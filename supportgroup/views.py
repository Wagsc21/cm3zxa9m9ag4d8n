
from django.shortcuts import render,get_object_or_404
from .forms import QueryForm,CommentForm,NotificationForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
	return render(request,'supportgroup/home.html')

@login_required(login_url='/accounts/login')
def queries(request):

	args = {}
	args.update(csrf(request))
	
	args['queries']= Query.objects.all()

	return render(request,'supportgroup/queries.html',args)

@login_required(login_url='/accounts/login')
def query(request, query_id = 1):
	return render(request, 'supportgroup/query.html',{'query' : get_object_or_404(Query,id=query_id)})


@login_required(login_url='/accounts/login')
def upvote(request,query_id, comment_id=0):
	if comment_id==0:
		p=get_object_or_404(Query,pk=query_id)
		voted=QueryUpvoteOrDownvote.objects.filter(user=request.user,query=p)
		if not voted.exists():
			p.upvotes +=1
			p.save()
			QueryUpvoteOrDownvote.objects.create(user=request.user,query=p,vote=1)
		return HttpResponseRedirect('/forum/home/queries/%s' % query_id)
	elif(int(comment_id)>0):
		p=get_object_or_404(Comment,pk=comment_id)
		voted=CommentUpvoteOrDownvote.objects.filter(user=request.user,comment=p)
		if not voted.exists():
			p.upvotes +=1
			p.save()
			CommentUpvoteOrDownvote.objects.create(user=request.user,comment=p,vote=1)
		return HttpResponseRedirect('/forum/home/queries/%s' % query_id)


@login_required(login_url='/accounts/login')
def downvote(request,query_id,comment_id=0):
	if(comment_id==0):	
		p=get_object_or_404(Query,pk=query_id)
		voted=QueryUpvoteOrDownvote.objects.filter(user=request.user,query=p)
		if not voted.exists():		
			p.downvotes +=1
			p.save()
			QueryUpvoteOrDownvote.objects.create(user=request.user,query=p,vote=0)
		return HttpResponseRedirect('/forum/home/queries/%s' % query_id)
	elif(int(comment_id)>0):
		p=get_object_or_404(Comment,pk=comment_id)
		voted=CommentUpvoteOrDownvote.objects.filter(user=request.user,comment=p)
		if not voted.exists():		
			p.downvotes +=1
			p.save()
			CommentUpvoteOrDownvote.objects.create(user=request.user,comment=p,vote=0)
		return HttpResponseRedirect('/forum/home/queries/%s' % query_id)



@login_required(login_url='/accounts/login')
def create(request):
	if request.POST:
		form = QueryForm(request.POST)
		# write form=QueryForm(request.POST,request.FILES) for including thumbnails
		if form.is_valid():
			form.save(request)
			return HttpResponseRedirect('/forum/home/queries/all')
	else:
		form = QueryForm()

	args = {}
	args.update(csrf(request))

	args['form'] = form
	
	return render(request, 'supportgroup/create_query.html', args)


@login_required(login_url='/accounts/login')
def comment(request,query_id):
	if request.POST:
		form = CommentForm(request.POST)
		form1 = NotificationForm(request.POST)
		if form.is_valid():
			form.save(request,query_id)
			return HttpResponseRedirect('/forum/home/queries/%s' % query_id)
			#name=form.cleaned_data['name']
			#body=form.cleaned_data['body']
			#pub_date=form.cleaned_data['pub_date']
			#query=Query.objects.get(id=query_id)
	else:
		form = CommentForm()
		form1 = NotificationForm()
	args = {}
	args['form'] = form
	args['query'] = Query.objects.get(id=query_id)
	return render(request, 'supportgroup/comment.html',args)



@login_required(login_url='/accounts/login')
def notifications(request):
	args = {}
	args['notifications']= Notification.objects.all()

	return render(request, 'supportgroup/notifications.html',args)


@login_required(login_url='/accounts/login')
def latest(request):
	latest_query_list = Query.objects.order_by('-pub_date')[:5]
	context = {'latest_query_list': latest_query_list,}
	return render(request,'supportgroup/latest.html',context)

















