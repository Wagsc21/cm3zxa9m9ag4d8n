from cbt2.models import  *
event_list = [line.rstrip('\n') for line in open('dbpopulator\eventlist.txt')]
#last_id=BeliefsEventsNats.objects.all().aggregate(Max('BeliefsEventsNatsID'))['BeliefsEventsNatsID__max']
for i in range(0,len(event_list)):
    BeliefsEventsNats.objects.get_or_create(beliefseventsnatsID=i+1,beliefseventsnats_text=event_list[i],category='event')

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
