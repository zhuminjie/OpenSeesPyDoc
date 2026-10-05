# -*- coding: utf-8 -*-
"""
This script implements the simplified hybrid p-y spring model for liquefied soils (Franke and Rollins, 2013) to simulate the response of 
a pile subjected to lateral spreading due to liquefaction, based on the shake table test of Abdoun et al. (2003).
The model uses a combination of p-y curves from Wang & Reese (1998) and Rollins (2005) to define the soil resistance along the pile length.
Results are verified against the numerical results shown in the paper by Franke and Rollins (2013) and the experimental data from Abdoun et al. (2003).

IMPORTANT: DOWNLOAD THE LATERAL SPREADING DISPLACEMENT DATA FILES FROM THE REPOSITORY AND PLACE THEM IN THE 'LATERALSPREAD' FOLDER BEFORE RUNNING THIS SCRIPT.

@author: Dr Alessandro Tombari (University of Exeter, UK)
@author: Dr Giovanni Nicosia Li Destri (COWI A/S Denmark)
@fund: COWI Fonden - Rapid Innovation Initiatives 


Keywords: Pile response; Liquefaction; Lateral spreading; Validation from centrifuge test;
 Verification of the simplified hybrid p-y spring model for liquefied soils (Franke and Rollins, 2013);
---------
REFERENCES:

[1]K. W. Franke and K. M. Rollins, “Simplified Hybrid p-y Spring Model for Liquefied Soils,” 
J. Geotech. Geoenviron. Eng., vol. 139, no. 4, pp. 564–576, Apr. 2013, doi: 10.1061/(ASCE)GT.1943-5606.0000750.

[2]T. Abdoun, R. Dobry, T. D. O’Rourke, and S. H. Goh, 
“Pile Response to Lateral Spreads: Centrifuge Modeling,” J. Geotech. Geoenviron. Eng., vol. 129, no. 10, pp. 869–878, Oct. 2003, 
doi: 10.1061/(ASCE)1090-0241(2003)129:10(869).
  
---------
MODEL 3b from Franke and Rollins (2013) paper, based on the shake table test of Abdoun et al. (2003):

  0_|_______|_________   
    | LOOSE |   Dr=40%
    | SAND  |   N160cs = 9.6
    |       | 
  6_|_______|_________
    |CEME   |
    | SAND  |  PHIeff=34.5 
 8_|_______ |  K=22.3 MN/m3

"""
#-------------

from unittest import case
import os
import numpy as np
import matplotlib.pyplot as plt
import openseespy.opensees as ops
from matplotlib.animation import FuncAnimation

#--------------------------------------------------------------
flagEuler = 1 # 1 (true) for Euler-Bernoulli beam, 0 for Timoshenko beam
flagTz = 1 # 0 (false) for no t-z springs, 1for t-z springs
TzTypeFlag = 1 # 1  t-z curve approximates Reese and O’Neill (1987); 2 approximates Mosher (1984) relation
flagLIN = [0,1] # 1 (true) for linear elastic soil, 0 for non linear soil (multilinear p-y curve)
Kinit = [None, 22.3e5] # Initial stiffness of the soil [Pa] - None: automatically computed from the p-y curve, otherwise user defined value
                                                                                                                                        
#-------------------------------------------------------------
# INPUT DATA
#-------------------------------------------------------------
# PILE DATA
Lpile = 8 #pile length Lpile > Lfree [m]
Dpile = 0.6 # pile diameter [m]
Lfree = 0.0 #free length pile >=0 (above z=0 ground surface)
Epile = 2E11 # Pile elastic modulus [Pa]
Ipile = 8E6/Epile # pile moment of inertia [m4]
Gpile = 8E10 # Pile shear modulus [Pa]
rhop = 0 # pile unit density [kgm-3] - consistency with Franke analysis
Apile = np.pi*Dpile**2/4 # pile cross section area [m2] - this value is not correct and no info is provided in the paper
Avpile = 3/4*Apile # pile shear area [m2]
nintpoints=8 #number of interpolation points used to define the Franke p-y curves
#-------------------------------------------------------------
# SOIL DATA
zLayerInterf =[0.,6.,8.] #depth of the interfaces between the soil layers (starting from z=0 at the ground surface, negative downwards) [m]
geff=[19500., 19500.] # average effective unit weight for each soil layer [N/m3]
J=[0.5,9.0]
N1_60=[9.6, 21.0]
phieff=[31.0, 34.5] # effective friction angle for each soil layer [degrees]
#------------------------------------------------------------
# ANALYSIS DATA
dz = 0.5 #mesh size
tEQ = 34.8 #duration of the seismic analysis [s]

#------------------------------------------------------------
# CALCULATION MAX SOIL PROFILE FOR P-Y CURVES
zdepth_list = [Lpile-i * dz for i in range(0,int(Lpile/dz))]
ylist=[]
for zi in zdepth_list:
    depth_str = f"{zi:.1f}"
    txt_path = os.path.join('./LATERALSPREAD/', f"tot_disp_depthm_{depth_str}.txt") #CHECK ALSO LINE 461
    col2 = np.genfromtxt(txt_path, skip_header=1, usecols=1)
    col2 = np.atleast_1d(col2)
    col2 = col2[~np.isnan(col2)]
    ylist.append(np.max(np.abs(col2)) if col2.size else 0.0)
    print(f'Loading lateral displacement data from {txt_path}')



#------------------------------------------------------------
#CALCULATED SOIL PARAMETERS

e50=[0.1537 * np.exp(-0.229 * N1_60[i]) for i in range(len(N1_60))]
for i in range(len(e50)):
    if e50[i] <= 0.0005:
        e50[i] = 0.0005
    elif e50[i] >= 0.05:
        e50[i] = 0.05

print('e50',e50)
#-------------------------------------------------------------
# HELPER FUNCTIONS 
#-------------------------------------------------------------
def calc_cu(geff,z):
    return geff*z*0.1 # 0.05 Boulanger 2007 ; 0.1 Ledezma and Bray (2010)

def calc_e50(N1_60):
    if N1_60 is None:
        return 0.05 #Boulanger 2007, for liquefied soil
    else:
        e50 = 0.1537 * np.exp(-0.229 * N1_60)
        if e50 <= 0.0005:
            e50 = 0.0005
        elif e50 >= 0.05:
            e50 = 0.05
        return e50

def CircularSection(D):
    A=np.pi*D**2/4
    I=np.pi*D**4/64
    Av=3/4*A
    return A,I,Av

def CircularHollowSection(D,t):
    A=np.pi*D**2/4-np.pi*(D-2*t)**2/4
    I=np.pi*D**4/64-np.pi*(D-2*t)**4/64
    Av=A*2/np.pi
    return A,I,Av

# Existing p-y Models for Liquefied Soil
def py_WangReese1998(dp:float,geff:float,cu:float,e50:float,J:float,z:float,y:float) -> float: 
    """
    Computes the p–y curve parameter according to Wang & Reese (1998).

    Parameters
    ----------
    dp: float
        Pile diameter
    geff : float
        average effective unit weight
    cu : float
        shear strength of the soil at depth z (represented by the residual shear strength Sr in the case of liquefied soil)
    e50 : float
        strain corresponding to one-half the maximum principal stress difference (0.05 for liquefied soil)
    J : float
        model factor typically equal to 0.5 for soft soils;
    z : float
        Depth below ground surface.    
    y : float
        Pile Lateral displacement

    Returns
    -------
    float
        Computed soil resistance per unit length of pile [N/m]
    """
    pu1 = (3+geff/cu*z+J/dp*z)*cu*dp
    pu2 = 9*cu*dp
    pu = np.min([pu1,pu2])
    p = 0.5*pu*(y/(2.5*e50*dp))**(1/3)
    return p


def py_Rollins2005(dp:float,z:float,y:float) -> float: 
    """
    Computes the p–y curve parameter according to Rollins (2005).

    Parameters
    ----------
    dp: float
        Pile diameter [m]
    z : float
        Depth below ground surface. [m]
    y : float
        Pile Lateral displacement [m]

    Returns
    -------
    float
        Computed soil resistance per unit length of pile [N/m]
    """
    y=y*1000 #transform m to mm
    A = 3e-7 * (z+1)**6.05
    B = 2.8*(z+1)**0.11
    C = 2.85*(z+1)**(-0.41)
    pd= 3.81*np.log(dp) + 5.6
    return A*(B*y)**C*pd*1000 #transform kN/m to N/m

def py_Franke2013(py1,py2):
    py = np.minimum(py1, py2)
    return py

def intersec_Franke2013(y,py1,py2,tol=1e-3):
    # Find the intersection point of two curves, tolerating near-zero differences (curves touching/overlapping)
    diff = np.subtract(py1, py2)
    for i in range(len(y)-1):
        if abs(diff[i]) <= tol:
            # Curves already coincide within tolerance at this point
            return y[i]
        if diff[i] * diff[i+1] < 0:
            # Linear interpolation to find the intersection point
            slope1 = (py1[i+1] - py1[i]) / (y[i+1] - y[i])
            slope2 = (py2[i+1] - py2[i]) / (y[i+1] - y[i])
            if abs(slope1 - slope2) <= tol:
                continue  # nearly parallel segments, skip to avoid division blow-up
            y_intersect = y[i] + (py2[i] - py1[i]) / (slope1 - slope2)
            #print('Intersection found at y =', y_intersect, 'm')
            return y_intersect
    if abs(diff[-1]) <= tol:
        return y[-1]
    return None  # No intersection found

def get_tzParam ( phi, b, sigV, pEleLength):
# references
#  Mosher, R.L. (1984). "Load transfer criteria for numerical analysis of
#   axial loaded piles in sand." U.S. Army Engineering and Waterways
#   Experimental Station, Automatic Data Processing Center, Vicksburg, Miss.
#
#  Kulhawy, F.H. (1991). "Drilled shaft foundations." Foundation engineering
#   handbook, 2nd Ed., Chap 14, H.-Y. Fang ed., Van Nostrand Reinhold, New York

  # Compute tult based on tult = Ko*sigV*pi*dia*tan(delta), where
  #   Ko    is coeff. of lateral earth pressure at rest, 
  #         taken as Ko = 0.4
  #   delta is interface friction between soil and pile,
  #         taken as delta = 0.8*phi to be representative of a 
  #         smooth precast concrete pile after Kulhawy (1991)
  
    delta = 0.8 * phi * np.pi/180

  # if z = 0 (ground surface) need to specify a small non-zero value of sigV

    if sigV == 0.0:
        sigV = 0.01
    
    tan_9 = np.tan(delta)
    tu = 0.4 * sigV * np.pi * b * tan_9
    
  # TzSimple1 material formulated with tult as force, not stress, multiply by tributary length of pile
    tult = tu * pEleLength

  # Mosher (1984) provides recommended initial tangents based on friction angle
	# values are in units of psf/in
    kf = [6000, 10000, 10000, 14000, 14000, 18000]
    fric = [28, 31, 32, 34, 35, 38]

    dataNum = len(fric)
    
    
	# determine kf for input value of phi, linear interpolation for intermediate values
    if phi < fric[0]:
        k = kf[0]
    elif phi > fric[5]:
        k = kf[5]
    else:
        for i in range(dataNum-1):
            if fric[i] <= phi and phi <= fric[i+1]:
                k = ((kf[i+1] - kf[i])/(fric[i+1] - fric[i])) * (phi - fric[i]) + kf[i]
        

  # need to convert kf to units of kN/m^3
    kSIunits =  k * 1.885

  # based on a t-z curve of the shape recommended by Mosher (1984), z50 = tult/kf
    z50 = tult / kSIunits

  # return values of tult and z50 for use in t-z material
    outResult = []
    outResult.append(tult)
    outResult.append(z50)

    return outResult
#-----------------------------------------------------------------------------------
# SET UP 
# ---------------------------------------------------------------------------------
ops.wipe()						       # clear opensees model
ops.model('basic', '-ndm', 3, '-ndf', 6)	       # 3 dimensions, 6 dof per node

#-----------------------------------------------------------------------------------
# GEOMETRY 
# -------------------------------------------------------------
# FREE PILE

if Lfree > 0:
    nfreenodes=int(Lfree/dz)
    zfreelist=[0.0 + i * dz for i in range(1, nfreenodes + 1)]
    if Lfree % dz != 0:
        zfreelist[-1]=Lfree  # Ensure the last node is at the pile tip

    for i,z in enumerate(zfreelist):
        ops.node(1000+i,0.,0.,z) #node free segment (tag starting from 1000)
    nfreenodes= len(zfreelist)
else:
    zfreelist=[]
    nfreenodes=0
    
# EMBEDDED PILE 

Lemb = Lpile - Lfree

if Lemb < 0:
    raise ValueError('Pile length incorrect, Lpile > Lfree')

nnodes=int(Lemb/dz)
zemblist=[-Lemb + i * dz for i in range(0, nnodes + 1)]
if Lemb % dz != 0:
    #print(Lemb,dz,Lemb % dz)
    zemblist[-1]=0.0  # Ensure the last node is at the ground surface (z=0)
    print('z=0 added')

#print(zemblist)
# -------------------------------------------------------------
# NODE GENERATION
for i,z in enumerate(zemblist):
    ops.node(i+1, 0.,0.,z)          

nnodes= len(zemblist)
#print('Pile nodes:',nnodes)
# SPI  
#plt.show()
for i,z in enumerate(zemblist): #Left side nodes (gap non modelled), index 2000
    ops.node(i+2000, -1 ,0.,z) 

# BOUNDARY CONDITIONS
for i,z in enumerate(zemblist): #Left side nodes (gap non modelled), index 2000
    ops.fix(i+2000, *(1, 1, 1,1, 1, 1)) 			           

ops.fix(1,*(0, 1, 1,0, 0, 1))                   #FIGURES SHOWN A NON-NULL ROTATION AT THE BASE, THE BASE IS FIXED ONLY IN TRANSLATION, NOT IN ROTATION
#-----------------------------------------------------------------------------------
# FINITE ELEMENTS 
# -------------------------------------------------------------
matPyTag=1 #starting tag for the uniaxial materials of the soil springs, will be incremented for each node
matTztag=matPyTag+nnodes+1 #starting tag for the uniaxial materials of the soil springs, will be incremented for each node
ops.geomTransf('Linear', 1,*(1,0,0))  		       #
# --------------------------------------------------------------------------------------                                    
# EMBEDDED PILE
if flagEuler == 0:
    print('PILE ELEMENTS: ElasticTimoshenkoBeam')
    #Apile,Ipile,Avpile=CircularSection(Dpile)
    for i in range(0,nnodes-1):
        ops.element('ElasticTimoshenkoBeam', i+1, i+1, i+2, Epile, Gpile, Apile,2*Ipile,Ipile,Ipile, Avpile,Avpile,1,'-mass',Apile*rhop)

    if Lfree > 0:
        for i in range(0,nfreenodes-1):
            ops.element('ElasticTimoshenkoBeam', i+1000, i+1000, i+1001, Epile, Gpile, Apile,2*Ipile,Ipile,Ipile, Avpile,Avpile,1,'-mass',Apile*rhop)

        ops.element('ElasticTimoshenkoBeam', i+1001, 1, 1000, Epile, Gpile, Apile,2*Ipile,Ipile,Ipile, Avpile,Avpile,1,'-mass',Apile*rhop)


else:
    print('PILE ELEMENTS: ElasticBeamColumn')
    for i in range(nnodes-1):
        ops.element('elasticBeamColumn',i+1, i+1, i+2,Apile, Epile,Gpile,2*Ipile,Ipile,Ipile,1,'-mass',Apile*rhop)

    if Lfree > 0:
        for i in range(0,nfreenodes-1):
            ops.element('elasticBeamColumn',i+1000, i+1000, i+1001,Apile, Epile,Gpile,2*Ipile,Ipile,Ipile,1,'-mass',Apile*rhop)
        ops.element('elasticBeamColumn',i+1001, 1, 1000,Apile, Epile,Gpile,2*Ipile,Ipile,Ipile,1,'-mass',Apile*rhop)
# --------------------------------------------------------------------------------------                                    
# SOIL SPRINGS DEFINITION
Eini=[]
geffi=0.
Ji=0.
e50i=0.
phieffi=0.
p1=[]
e1=[]
for i in range(0,nnodes-1): #first node zero resistance
        if ylist[i] < 0.05:
            ymax = 0.05 #avoid zero division in p-y curve definition
        else:            
            ymax = ylist[i]
            print('ymax',ymax,'at z=',zemblist[i])
        # Include 0 explicitly, then use geometric spacing for the remaining points.
        ypile = np.insert(np.geomspace(ymax / 1000.0, ymax, nintpoints), 0, 0.0)
        zi=np.abs(zemblist[i])
        print('zi',zi)
        for ii in range(len(zLayerInterf)-1):
            if zLayerInterf[ii] <= zi <= zLayerInterf[ii+1]:
                geffi=geff[ii]
                e50i=e50[ii]
                Ji=J[ii]
                phieffi=phieff[ii]
                flagS=flagLIN[ii]
                print('layer is between',zLayerInterf[ii], 'and', zLayerInterf[ii+1])
                break
            elif zi > zLayerInterf[-1]:
                geffi=geff[-1]
                e50i=e50[-1]
                Ji=J[-1]
                phieffi=phieff[-1]
                flagS=flagLIN[-1]
                print('layer is below',zLayerInterf[-1])
                break
            #else:
                #raise ValueError('Depth z='+str(zi)+' m is out of the defined soil layers, check zLayerInterf')
        cui = calc_cu(geffi, zi)
        # --------------------------------------------------------------------------------------  
        # PY CURVE DEFINITION        
        pRol=[py_Rollins2005(Dpile,zi,yi) for yi in np.linspace(0.01,ymax,1000)]      
        pWR=[py_WangReese1998(Dpile,geffi,cui,e50i,Ji,zi,yi) for yi in np.linspace(0.01,ymax,1000)]
        yintersect=intersec_Franke2013(np.linspace(0.01,ymax,1000),pRol,pWR)
        if  yintersect is not None:
            if yintersect < ymax and yintersect > 0.01:
                ypile=np.append(ypile, yintersect)
        else:
            print('No intersection found for z=',zi)                            
        ypile.sort()
        #print([ypile[0],ypile[1],ypile[2],ypile[3] ])
        pRol=[py_Rollins2005(Dpile,zi,yi) for yi in ypile]
        pWR=[py_WangReese1998(Dpile,geffi,cui,e50i,Ji,zi,yi) for yi in ypile]
        pFr=py_Franke2013(pRol,pWR)
        #pFr=pWR
        # --------------------------------------------------------------------------------------  
        # TZ CURVE DEFINITION 
        # vertical effective stress at current depth    
        sigV = geffi * zi
        # procedure to define tult and z50
        tzParam = get_tzParam(phieffi, Dpile, sigV, dz)
        tult = tzParam [0]
        z50 = tzParam [1]
        ops.uniaxialMaterial('TzSimple1', matTztag+i, TzTypeFlag, tult, z50, 0.0)

  

        pts = [x for idx in range(1,len(ypile)) for x in (ypile[idx], np.multiply(pFr[idx], dz))]
        p1.append(pFr[1])
        e1.append(ypile[1])
        #print(f'{pFr[1]:.2e}-{ypile[1]:.2e}')
        #plt.plot([pts[i] for i in range(0,8,2)],[pts[i] for i in range(1,8,2)] ,'^')
        #print(pts) 
        # UNCOMMENT TO PLOT PY CURVE AT EACH NODE (they are many, so not plotted by default)
        if 1.9 < zi<=2.1: #plot only for a few nodes, otherwise too many plots
            plt.figure(i+100)
            plot_title = f'dynpy curve at z>{zi:.1f} m'
            plt.title(plot_title)
            yp=np.linspace(0,ymax,100)
            pRolC=np.array([py_Rollins2005(Dpile,zi,yi) for yi in yp])
            pWRC=np.array([py_WangReese1998(Dpile,geffi,cui,e50i,Ji,zi,yi) for yi in yp])
            pFrC=np.array(py_Franke2013(pRolC,pWRC))
            plt.plot(ypile,np.multiply(pFr, 1),'*--k')
            plt.plot(yp,np.multiply(pFrC, 1),'-r')
            plt.plot(yp,np.multiply(pRolC, 1),':b')
            plt.plot(yp,np.multiply(pWRC, 1),':g')
            plt.legend(['p-y curve - Numerical','p-y curve - Franke 2013', 'p-y curve - Rollins 2005','p-y curve - Wang & Reese 1998'])
            plt.ylim([0, 1.2*np.max(pFrC)])
            plt.xlabel('lateral displacement [m]')
            plt.ylabel('soil resistance [N/m]')                                              
            plot_filename = plot_title.replace(' ', '_').replace('>', '') + '.png'
            plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
        #     plt.show()
        
        match flagS:
            case 1:
                    if Kinit[ii] is not None:
                        Eini.append(Kinit[ii]) #user defined initial stiffness of the soil at each node, used for the elastic link definition (not shown in the paper, but useful to have an idea of the stiffness of the soil at each node, and to plot it)    
                        ops.uniaxialMaterial('Elastic', matPyTag+i, Eini[-1]*dz)   
                    #Eini.append(1.8e4*zi**.5) 
                    else:
                        Eini.append(pFr[1]/ypile[1]*dz) #initial stiffness of the soil at each node, used for the elastic link definition (not shown in the paper, but useful to have an idea of the stiffness of the soil at each node, and to plot it)
                        ops.uniaxialMaterial('Elastic', matPyTag+i,  Eini[-1])   
                    print(f'node {i+1} at depth {zi:.2f} m, linear soil, stiffness {Eini[-1]:.2e} N/m2')
            case 0:
                    if Kinit[ii] is not None:
                        Eini.append(Kinit[ii]) #user defined initial stiffness of the soil at each node, used for the elastic link definition (not shown in the paper, but useful to have an idea of the stiffness of the soil at each node, and to plot it)    
                        ptsi=pts.copy()
                        ptsi[1]=Eini[-1]*ypile[1]/dz #initial stiffness of the soil at each node, used for the elastic link definition (not shown in the paper, but useful to have an idea of the stiffness of the soil at each node, and to plot it)
                        ops.uniaxialMaterial('MultiLinear', matPyTag+i,*ptsi)
                    else:
                        ops.uniaxialMaterial('MultiLinear', matPyTag+i, *pts)
                        Eini.append(pFr[1]/ypile[1]*dz) #initial stiffness of the soil at each node, used for the elastic link definition (not shown in the paper, but useful to have an idea of the stiffness of the soil at each node, and to plot it)
                    print(f'node {i+1} at depth {zi:.2f} m, non linear soil, initial stiffness {Eini[-1]:.2e} N/m2')
        match flagTz:
            case 1:
                    ops.element('twoNodeLink', 3000+i, i+1, i+2000, '-mat', matPyTag+i, matPyTag+i,matTztag+i,'-dir', *(1,2,3))
            case 0:
                    ops.element('twoNodeLink', 3000+i, i+1, i+2000, '-mat', matPyTag+i, matPyTag+i,'-dir', *(1,2))

#-----------------------------------------------------------------------------------
# TIME INTEGRATION SEISMIC ANALYSIS 
# -------------------------------------------------------------
ops.loadConst('-time', 0.0)				# if EQ analysis, hold gravity constant and restart time to 0s
ops.wipeAnalysis()         
# GROUND MOTION Multi Support---------------------------------------------------------------------
ops.pattern('MultipleSupport', 2)
# Application GM displ at each side of the springs of the pile 
for i in range(0,nnodes-1):
    depth = Lpile-i * dz
    depth_str = f"{depth:.1f}"
    txt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'LATERALSPREAD', f"tot_disp_depthm_{depth_str}.txt")

    dataf=np.genfromtxt(txt_path,skip_header=1)
    dataf = dataf[~np.isnan(dataf).any(axis=1)]
    timeX=list(dataf[:,0])
    displX=list(dataf[:,1])  
    ops.timeSeries('Path', i,   '-time', *timeX, '-values', *displX,'-prependZero')     
    ops.groundMotion(1+i,'Plain', '-disp', i)                   #define timeseries as displacements
    ops.imposedMotion(i+2000, 1, 1+i)        # Left Spring

nSteps = len(timeX)
print('Number of time steps:', nSteps)
ops.constraints('Transformation')  				# how it handles boundary conditions
ops.numberer('Plain')			    # renumber dof's to minimize band-width (optimization), if you want to
ops.system('BandGeneral')		    # how to store and solve the system of equations in the analysis
ops.test('NormDispIncr', 1.0e-4,  200, 5 )
ops.algorithm('Newton')                # use NONLinear algorithm for NONlinear analysis
ops.integrator('Newmark',0.5,0.25)
ops.analysis('Transient')   # define type of analysis: time-dependent
topdisp=[]
linkF=[]
linkD=[]
piledispl_hist=[]
bendingM_hist=[]
grounddisp_hist=[]
tCurrent = ops.getTime()
disp_history_X = np.zeros((nSteps, nnodes))  # Store displacements for each node at each time step
BM_history = np.zeros((nSteps, nnodes))
original_coords = np.zeros((nnodes, 3))
for nodetag in range(1,nnodes+1):
    x, y, z = ops.nodeCoord(nodetag)
    original_coords[nodetag-1,:] = [x , y, z]

completed_steps = 0
while tCurrent < tEQ:
    ok = ops.analyze(1, .01)
    tCurrent = ops.getTime()
    #print('time',tCurrent)

    if ok != 0:
        print('noncovergence')
        tCurrent=100
        print('collapse')
    
    completed_steps = completed_steps + 1
    di=ops.nodeDisp(nnodes,1)
    dsoil_i = ops.nodeDisp(nnodes+2000-2,1)
    #print('dsoil',dsoil_i,'top disp',di)
    #print('load factor',ops.getLoadFactor(1),'time',ops.getTime())
    topdisp.append(di)
    grounddisp_hist.append(dsoil_i)
    linkF.append(-ops.eleResponse(3000+nnodes-5, 'localForce')[0])
    linkD.append(-ops.eleResponse(3000+nnodes-5, 'localDisplacement')[0])

    piledispl_i=[]
    for i in range(0,nnodes):
        piledispl_i.append(ops.nodeDisp(i+1,1))
    piledispl_hist.append(piledispl_i)

    bendingM_i=[]
    for i in range(0,nnodes-1):
        bendingM_i.append(ops.eleForce(i+1,5)) #bending moment along the pile
    bendingM_i.append(ops.eleForce(i+1,11)) #bending moment at the top of the pile
    bendingM_hist.append(bendingM_i)

    for nodetag in range(1,nnodes+1):
        ux = ops.nodeDisp(nodetag, 1)
        uy = ops.nodeDisp(nodetag, 2)
        disp_history_X[completed_steps-1, nodetag-1] = ux
        #disp_history[completed_steps, nodetag, 1] = uy
        BM_history[completed_steps-1, nodetag-1] = ops.eleForce(nodetag, 5)
    BM_history[completed_steps-1, nodetag-1] = ops.eleForce(nodetag, 11)  # bending moment at the top of the pile

disp_history_X = disp_history_X[:completed_steps]
BM_history = BM_history[:completed_steps]

#-----------------------------------------------------------------------------------
# POST PROCESSING - GRAPHICS - GIF ANIMATION generation
# -------------------------------------------------------------

#animation of the pile displacement  over time

nframes = len(linkF)


fig, ax = plt.subplots()

line_displ, = ax.plot([], [], '-k', lw=2)
scale = 1.0  # Adjust this scale factor as needed

# Set fixed plotting limits
x_min = np.min(original_coords[:, 0])
x_max = np.max(original_coords[:, 0])
z_min = np.min(original_coords[:, 2])
z_max = np.max(original_coords[:, 2])
y_min = np.min(original_coords[:, 1])
y_max = np.max(original_coords[:, 1])

max_disp = np.max(np.abs(disp_history_X))

ax.set_xlim(
x_min - scale * max_disp - 0.1,
x_max + scale * max_disp + 0.1
)
ax.set_ylim(z_min, z_max)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel('Lateral displacement, X (m)')
ax.set_ylabel('Depth, Z (m)')
ax.grid(True)



def update_piledisp(frame):

    x = (
        original_coords[:, 0]
        + scale * disp_history_X[frame, :]
    )

    # No vertical displacement is currently stored
    z = original_coords[:, 2]

    line_displ.set_data(x, z)

    return line_displ,




ani = FuncAnimation(
    fig,
    update_piledisp,
    frames=range(0, nframes, 10), 
    interval=20,
    blit=True
)

ani.save("pileD_Dynamic_animation.gif", writer="pillow", fps=20)

#ANIMATION FOR BENDING MOMENT ALONG THE PILE OVER TIME

fig2, ax2 = plt.subplots()

line_BM_Dynamic, = ax2.plot([], [], '-k', lw=2, label='Dynamic')
line_BM_EnVDynamic, = ax2.plot([], [], '--r', lw=2, label='Envelope-Dynamic')

def update_pileBM(frame):

    BM = BM_history[frame, :]
    z  = original_coords[:, 2]

    BM = np.nan_to_num(BM, nan=0.0)
    BM_EnVD = np.min(BM_history[:frame+1, :], axis=0)
    BM_EnVD = np.nan_to_num(BM_EnVD, nan=0.0)

    line_BM_Dynamic.set_data(BM, z)
    line_BM_EnVDynamic.set_data(BM_EnVD, z)

    return line_BM_Dynamic, line_BM_EnVDynamic

#BM_history = np.nan_to_num(BM_history, nan=0.0)
max_BM = np.nanmax(np.abs(BM_history))
print('max bending moment is', max_BM, 'N.m')

ax2.set_xlim(
-max_BM*1.1,
max_BM*1.1
)
ax2.set_ylim(z_min, z_max)
ax2.set_aspect('auto')
ax2.set_xlabel('Bending Moment, M (N.m)')
ax2.set_ylabel('Depth, Z (m)')
ax2.grid(True)
ax2.legend(loc='upper right', fontsize=10)

ani2 = FuncAnimation(
    fig2,
    update_pileBM,
    frames=range(0, nframes, 10), 
    interval=20,
    blit=False
)
#ani.save("response.mp4", writer="ffmpeg", fps=30)
ani2.save("pileBM_Dynamic_animation.gif", writer="pillow", fps=20)

#ANIMATION FOR P-Y CURVE AT A SPECIFIC DEPTH OVER TIME

fig3, ax3 = plt.subplots()

line_PY, = ax3.plot([], [], '-k', lw=2)
pointPY, = ax3.plot([], [], 'ro')

def update_PY(frame):

    PY_F = linkF[:frame+1]
    PY_D = linkD[:frame+1]

    line_PY.set_data(PY_D, PY_F)

    pointPY.set_data([linkD[frame]],[linkF[frame]])

    return line_PY, pointPY

#BM_history = np.nan_to_num(BM_history, nan=0.0)
max_D = np.max(np.abs(linkD))
print('max displacement is', max_D, 'm')
max_F = np.max(np.abs(linkF))
print('max force is', max_F, 'N')

ax3.set_xlim(
-max_D*1.1,
max_D*1.1
)
ax3.set_ylim(
-max_F*1.1,
max_F*1.1
)
ax3.set_aspect('auto')
ax3.set_ylabel('Link Force, F (N)')
ax3.set_xlabel('Link Displacement, D (m)')
ax3.set_title('P-Y Curve at z = {:.2f} m'.format(zemblist[-5]))  # Example depth, adjust as needed
ax3.grid(True)


ani3 = FuncAnimation(
    fig3,
    update_PY,
    frames=range(0, nframes, 10), 
    interval=20,
    blit=False
)
#ani.save("response.mp4", writer="ffmpeg", fps=30)
ani3.save("pilePY_Dynamic_animation.gif", writer="pillow", fps=20)


plt.show()
