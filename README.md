# Drift Chat Widget
Easily add Drift's chat widget to your Django apps.


## Getting Started
To get started run `pip install django-drift-chatwidget`


### Settings
In your `settings.py` file add the following lines:

```
DRIFT_CHAT_WIDGET = {
    'ID': '[YOUR ID]',
    'SNIPPET_VERSION': '[SNIPPET VERSION]'
}
```

Your `ID` and `SNIPPET_VERSION` can be obtained [here](https://app.drift.com/settings/widget) in the **JavaScript** section.
*Note: The values in `drift.load('YOUR ID');` represent your `ID`*

Lastly, add `drift_chatwidget` to your `INSTALLED_APPS` section.


### Templates
```
{% load drift_chat_widget %}
{% drift_chatwidget %}
```

You should now be able to see the chat widget on pages where the template tag is included.

### Bugs
If you find a bug, feel free to suggest a fix or contribute by opening up a PR.


### Contributors
- Lemuel Boyce [rhymiz](https://github.com/rhymiz)
