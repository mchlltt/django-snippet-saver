# iSnippets - Homework instructions

### Overview

Your homework for the week is to use Django to build a CRUD application that allows you to create, view, update, and delete useful code snippets. Think of it as the MVP for an app you'd use to keep track of idiomatic code samples in different languages.

### Preliminary Notes

Since you're learning both a new language _and_ a new framework, the basic requirements for this week's homework assignment are fairly straightforward. 

You'll see two "tiers" listed below. Think of these as milestones. The first corresponds with basic competency with Django's essential features. The second corresponds to familiarity with the tools you'll be using in real projects. This is the level you must achieve to receive full credit on the homework assignment. Consider them "checkpoints" for your homework progress—Tier 1 lays a foundation, while Tier 2 reinforces it.

As always, feel free to Slack TAs or instructors if you get stuck. Keep [Django's superb documentation](https://docs.djangoproject.com/en/1.10/) handy, and best of luck!

### Instructions

#### Tier 1

Create an application that allows you to create and save code snippets. 

Each code snippet should allow the user to record a title; the language the snippet is in; the snippet itself; and a brief description. Make sure that, in your views, your snippets display properly. You'll need to wrap the code snippet in HTML `<pre>` tags to accomplish this.

#### Tier 2

Make sure your application uses Django's form helpers and generic views wherever possible.