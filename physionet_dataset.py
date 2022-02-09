#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

from aif360.datasets import StandardDataset


# In[4]:


class PhysionetDataset(StandardDataset):


    def __init__(self, label_name='return.to.emergency.department.within.6.months', 
                 favorable_classes=[1],
                 protected_attribute_names=['ageCat'],
                 privileged_classes=[['weight'], lambda x: x > 60],
                 instance_weights_name=None,
                 categorical_features=['DestinationDischarge', 'admission.ward', 'admission.way',
                                      "occupation", "discharge.department", "visit.times", "gender",
                                      "type.of.heart.failure", "NYHA.cardiac.function.classification",
                                      'Killip.grade'],
                 features_to_keep=[], features_to_drop=[],
                 na_values=[], custom_preprocessing=None,
                 metadata=None):
 

       # filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
       #                         '..', 'data', 'raw', 'german', 'german.data')
        
        filepath = ('PhysioNetDataEdited.csv')

        column_names = ['DestinationDischarge', 'admission.ward', 'admission.way', 'occupation',
                           'discharge.department', 'visit.times', 'gender', 'body.temperature',
                           'pulse', 'respiration', 'map', 'weight', 'height', 'BMI',
                           'type.of.heart.failure', 'NYHA.cardiac.function.classification',
                           'Killip.grade', 'myocardial.infarction', 'congestive.heart.failure',
                           'peripheral.vascular.disease', 'cerebrovascular.disease', 'dementia',
                           'Chronic.obstructive.pulmonary.disease', 'connective.tissue.disease',
                           'peptic.ulcer.disease', 'diabetes',
                           'moderate.to.severe.chronic.kidney.disease', 'hemiplegia',
                           'malignant.lymphoma', 'solid.tumor', 'liver.disease', 'AIDS',
                           'type.II.respiratory.failure', 'consciousness', 'eye.opening',
                           'movement', 'respiratory.support.', 'oxygen.inhalation', 'fio2',
                           'acute.renal.failure', 'left.ventricular.end.diastolic.diameter.LV',
                           'outcome.during.hospitalization',
                           'return.to.emergency.department.within.6.months',
                           'creatinine.enzymatic.method', 'urea', 'uric.acid',
                           'glomerular.filtration.rate', 'cystatin', 'monocyte.ratio',
                           'lymphocyte.count', 'mean.hemoglobin.volume',
                           'mean.hemoglobin.concentration', 'mean.platelet.volume',
                           'basophil.count', 'eosinophil.count', 'hemoglobin',
                           'platelet.distribution.width', 'platelet.hematocrit',
                           'neutrophil.count', 'D.dimer', 'international.normalized.ratio',
                           'activated.partial.thromboplastin.time', 'thrombin.time',
                           'prothrombin.activity', 'fibrinogen', 'carbon.dioxide.binding.capacity',
                           'calcium', 'potassium', 'sodium',
                           'creatine.kinase.isoenzyme.to.creatine.kinase',
                           'hydroxybutyrate.dehydrogenase.to.lactate.dehydrogenase',
                           'hydroxybutyrate.dehydrogenase', 'glutamic.oxaloacetic.transaminase',
                           'creatine.kinase', 'creatine.kinase.isoenzyme',
                           'brain.natriuretic.peptide', 'nucleotidase', 'fucosidase',
                           'white.globulin.ratio', 'glutamyltranspeptidase',
                           'glutamic.pyruvic.transaminase', 'alkaline.phosphatase',
                           'total.bilirubin', 'total.bile.acid', 'total.protein',
                           'low.density.lipoprotein.cholesterol', 'triglyceride',
                           'high.density.lipoprotein.cholesterol', 'ageCat']
        try:
            df = pd.read_csv(filepath, sep=' ', header=None, names=column_names,
                             na_values=na_values)
        except IOError as err:
            print("IOError: {}".format(err))
            print("To use this class, please download the following files:")
            print("\n\thttps://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data")
            print("\thttps://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.doc")
            print("\nand place them, as-is, in the folder:")
            print("\n\t{}\n".format(os.path.abspath(os.path.join(
                os.path.abspath(__file__), '..', '..', 'data', 'raw', 'german'))))
            import sys
            sys.exit(1)

        super(PhysionetDataset, self).__init__(df=df, label_name=label_name,
            favorable_classes=favorable_classes,
            protected_attribute_names=protected_attribute_names,
            privileged_classes=privileged_classes,
            instance_weights_name=instance_weights_name,
            categorical_features=categorical_features,
            features_to_keep=features_to_keep,
            features_to_drop=features_to_drop, na_values=na_values,
            custom_preprocessing=custom_preprocessing, metadata=metadata)


# In[ ]:




