# file for populating G:\makeblog\final2\cbt2 admin.py model Cognitivedistortion
from cbt2.models import Cognitivedistortion
Cognitivedistortion_list=[
    'Mind reading.',
    'Overgeneralization.',
    'Fortune telling/ Future prediction.',
    'All or none thinking',
    'Jumping to conclusions.',
    'Catastrophizing.',
    'Self blame/ Personalization.',
    'Should statement.',
    'Emotional reasoning.',
    'Magnification or minimization',
    'Mental filter.',
    'Disqualifying the positive.',
    ]
for i in range(0,len(Cognitivedistortion_list)):
    Cognitivedistortion.objects.create(cognitivedistortionID=i+1,cognitivedistortion_text=Cognitivedistortion_list[i])
