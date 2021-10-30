from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect
from django.template import loader
from .models import Post
from booking.forms import BookingForm
from booking.models import Booking
from django.urls import reverse

# Create your views here.
def indexView(request):
  posts = Post.objects.all()
  template = loader.get_template('index.html')
  context = {
		'posts': posts,
	}
  
  return HttpResponse(template.render(context, request))



def PostDetails(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  
  if request.method == 'POST':
    form = BookingForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data.get('name')
      email = form.cleaned_data.get('email')
      meeting_time = form.cleaned_data.get('meeting_time')
      meeting_date = form.cleaned_data.get('meeting_date')
      remarks = form.cleaned_data.get('remarks')

      booking = form.save(commit=False)
      booking.post = post
      booking.save()
			
      return HttpResponseRedirect(reverse('postdetails', args=[post_id]))
  
  
  else:
    form = BookingForm()
      
      
  context = {
    'post':post,
    'form':form,
  }
  template = loader.get_template('postdetails.html')

  return HttpResponse(template.render(context, request))





