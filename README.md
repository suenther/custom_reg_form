
This custom registration form, forked from https://github.com/open-craft/custom-form-app ,and modifed for Tutor Open edX. It works with Python3 and Open edX Koa.
You can add new fields to your register form, and download all information from the Django admin site as a CSV file.

Please test it before using in production!


## Installation on tutor:

### app installation:

```bash
cd .local/share/tutor/env/build/openedx/requirements   

git clone  https://github.com/murat-polat/custom-form-app 

echo "-e ./custom_reg_form" >>  private.txt 

pip install -e custom_reg_form
```

### plugin activation

```bash
tutor plugins printroot # ~/.local/share/tutor-plugins

mkdir "$(tutor plugins printroot)"

cp custom_reg_form/custom_form_plugin.yml $(tutor plugins printroot)

tutor plugins list

tutor plugins enable custom_reg_form_plugin
tutor config save
tutor images build openedx

tutor local start
```

If all done right you should see the migrations after `tutor local start`


### Debug and development:

`tutor local run lms bash `

`./manage.py lms makemigrations custom_reg_form`

`./manage.py lms migrate `

To delete and recreate migrations:


`./manage.py lms migrate custom_reg_form zero `

Than

`./manage.py lms makemigrations custom_reg_form `

`./manage.py lms migrate`

![](src/custom_reg.gif)
