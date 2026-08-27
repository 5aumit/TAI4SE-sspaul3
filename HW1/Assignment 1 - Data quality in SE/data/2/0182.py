from django.contrib.auth.decorators import user_passes_test
from crequest.middleware import CrequestMiddleware


def group_required(group_names):
	"""Requires user membership in at least one of the groups passed in."""
	try:
		user = CrequestMiddleware.get_request().user
		if user.is_authenticated():
			test = user.groups.filter(name=group_names).exists()
	except (AttributeError):
		test = False


	return user_passes_test(test)