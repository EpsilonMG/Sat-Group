#!/usr/bin/env python
# coding: utf-8

# In[1]:


Smoking_dummies={
    'Yes':[1],
    'No':[0]
}
AlcoholDrinking_dummies={
    'Yes':[1],
    'No':[0]
}

Sex_dummies={
    'Male':[1],
    'Female':[0]
}
PhysicalHealth_dummies={
    'Mild degree':[1,0,0,0],
    'Moderate degree':[0,1,0,0],
    'Normal degree':[0,0,1,0],
    'Severe degree':[0,0,0,1],
    'Marked degree':[0,0,0,0]
}


AgeCategory_dummies={
    '18-24':[0,0,0,0,0,0,0,0,0,0,0,0],
    '25-29':[1,0,0,0,0,0,0,0,0,0,0,0],
    '30-34':[0,1,0,0,0,0,0,0,0,0,0,0],
    '35-39':[0,0,1,0,0,0,0,0,0,0,0,0],
    '40-44':[0,0,0,1,0,0,0,0,0,0,0,0],
    '45-49':[0,0,0,0,1,0,0,0,0,0,0,0],
    '50-54':[0,0,0,0,0,1,0,0,0,0,0,0],
    '55-59':[0,0,0,0,0,0,1,0,0,0,0,0],
    '60-64':[0,0,0,0,0,0,0,1,0,0,0,0],
    '65-69':[0,0,0,0,0,0,0,0,1,0,0,0],
    '70-74':[0,0,0,0,0,0,0,0,0,1,0,0],
    '75-79':[0,0,0,0,0,0,0,0,0,0,1,0],
    '80 or older':[0,0,0,0,0,0,0,0,0,0,0,1]
}
Race_dummies={
    'Asian'   :[1,0,0,0,0],
    'Black'   :[0,1,0,0,0],
    'Hispanic':[0,0,1,0,0],
    'Other'   :[0,0,0,1,0],
    'White'   :[0,0,0,0,1],
    'American Indian/Alaskan Native'   :[0,0,0,0,0]
}
Diabetic_dummies={
    'No':[0,0,0],
    'No, borderline diabetes':[1,0,0] ,
    'Yes':[0,1,0],
    'Yes (during pregnancy)':[0,0,1]
}
PhysicalActivity_dummies={
    'Yes':[1],
    'No':[0]
}    
GenHealth_dummies={    
    'Fair':[1,0,0,0],
    'Good':[0,1,0,0],
    'Poor':[0,0,1,0],
    'Very good':[0,0,0,1],
    'Excellent':[0,0,0,0]
}


