.. include:: sub.txt

=======================
 Run all model button
=======================

This button is at the top left corner of
the cloud viewer.

This button will run all the scripts for all models.

The order of scripts that are run are as follow:

1. :doc:`ViewerSetting`
1. :doc:`GenericModel`
1. :doc:`AnalysisSetting`
1. :doc:`runAnalysisModule`
1. :doc:`PlotModule`

For the same module type, the modules with lower `id`
is run before the ones with larger `id`.
