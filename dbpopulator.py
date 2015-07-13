from cbt2.models import  *
"""
it is a database population file which has to be run like this
cd/"path to the project directory"
run command : python manage.py shell
then copy this code and paste it in the command prompt interactive shell
this file will populate cbt2/models/BeliefsEventsNats table 
it will read input from the text files in the dbpopulator folder.
this is a one time use file it can only be used to create initial database rows
to change you have to add or delete the row from the admin site 127.0.0.1:8000/admin
"""
try :
    last_id=BeliefsEventsNats.objects.all().aggregate(Max('beliefseventsnatsID'))['beliefseventsnatsID__max']
except:
    last_id=0
event_list = [line.rstrip('\n') for line in open('dbpopulator\eventlist.txt')]
#last_id=BeliefsEventsNats.objects.all().aggregate(Max('BeliefsEventsNatsID'))['BeliefsEventsNatsID__max']
for i in range(0,len(event_list)):
    BeliefsEventsNats.objects.get_or_create(beliefseventsnatsID=last_id+i+1,beliefseventsnats_text=event_list[i],category='event')

last_id=BeliefsEventsNats.objects.all().aggregate(Max('beliefseventsnatsID'))['beliefseventsnatsID__max']
persistentnat_list = [line.rstrip('\n') for line in open('dbpopulator\persistentnat.txt')]
for i in range(0,len(persistentnat_list)):
    BeliefsEventsNats.objects.get_or_create(beliefseventsnatsID=last_id+i+1,beliefseventsnats_text=persistentnat_list[i],category='persistentnat')
    
    
last_id=BeliefsEventsNats.objects.all().aggregate(Max('beliefseventsnatsID'))['beliefseventsnatsID__max']
corebelief_list = [line.rstrip('\n') for line in open('dbpopulator\Corebelief.txt')]
for i in range(0,len(corebelief_list)):
    BeliefsEventsNats.objects.get_or_create(beliefseventsnatsID=last_id+i+1,beliefseventsnats_text=corebelief_list[i],category='corebelief')
    
    
last_id=BeliefsEventsNats.objects.all().aggregate(Max('beliefseventsnatsID'))['beliefseventsnatsID__max']
intermediatebelief_list = [line.rstrip('\n') for line in open('dbpopulator\Intermediatebelief.txt')]
for i in range(0,len(intermediatebelief_list)):
    BeliefsEventsNats.objects.get_or_create(beliefseventsnatsID=last_id+i+1,beliefseventsnats_text=intermediatebelief_list[i],category='intermediatebelief')
