from rest_framework.utils.serializer_helpers import ReturnDict

from {{cookiecutter.project_slug}}.users.models import BaseUser
from {{cookiecutter.project_slug}}.users.selectors import get_profile as get_profile_selector
from {{cookiecutter.project_slug}}.users.serializers import ProfileOutputSerializer


def get_profile(user: BaseUser) -> ReturnDict:
    profile = get_profile_selector(user=user)
    return ProfileOutputSerializer(profile).data
