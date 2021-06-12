from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, state_choices, bedroom_choices

from .models import Listing


def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)
	
	paginator = Paginator(listings, 5)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)
	
	context = {
		"listings": paged_listings
	}
	
	return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
	listing = get_object_or_404(Listing, pk=listing_id)
	
	# getting internal photos
	internal_photos = []
	for i in range(1, 7):
		if getattr(listing, 'photo_%d' % i):
			photo = getattr(listing, 'photo_%d' % i)
			internal_photos.append(photo)
	
	context = {
		'listing': listing,
		'internal_photos': internal_photos
	}
	return render(request, 'listings/listing.html', context)


def search(request):
	query_set_list = Listing.objects.order_by('-list_date')
	# keywords search
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		query_set_list = query_set_list.filter(description__contains=keywords)
	
	# city search
	if 'city' in request.GET:
		city = request.GET['city']
		query_set_list = query_set_list.filter(city__iexact=city)
	
	# state search
	if 'state' in request.GET:
		state = request.GET['state']
		query_set_list = query_set_list.filter(state__iexact=state)
	
	# bedroom search
	if 'bedrooms' in request.GET:
		bedrooms = request.GET['bedrooms']
		query_set_list = query_set_list.filter(bedrooms__lte=bedrooms)
	
	# price search
	if 'price' in request.GET:
		price = request.GET['price']
		query_set_list = query_set_list.filter(price__lte=price)
	
	context = {
		'price_choices': price_choices,
		'state_choices': state_choices,
		'bedroom_choices': bedroom_choices,
		'listings': query_set_list,
		'values': request.GET,
	}
	return render(request, 'listings/search.html', context)
