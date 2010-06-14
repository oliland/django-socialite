from distutils.core import setup



setup(
    name = "django-socialite",
    version = "0.1a",
    author = "oliland",
    author_email = "oli@oliland.net",
    description = "Easy sign-ins with Facebook, LinkedIn and Twitter based on oauth-access",
    long_description = open("README.md").read(),
    license = "BSD",
    url = "http://github.com/oliland/django-socialite",
    packages = [
        "socialite",
        "socialite.facebook_user",
        "socialite.linkedin_user",
        "socialite.twitter_user",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
