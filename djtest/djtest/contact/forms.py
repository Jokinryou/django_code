# -*- coding:utf-8 -*-

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")

        #It’s important that we explicitly return the cleaned value for the field at
        #the end of this method. This allows us to modify the value (or convert it to
        #a different Python type) within our custom validation method.
        #If we forget the return statement, then None will be returned,
        #and the original value will be lost.
        return message
