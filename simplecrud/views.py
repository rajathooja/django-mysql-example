from django.shortcuts import render
from .forms import DatabaseForm


# Create your views here.
def showform(request):

    """ initialize a user feedback variable """
    status = ""

    # if the user has POSTed data
    if request.method == 'POST':

        # initialize the ModelForm object
        form = DatabaseForm(request.POST or None)

        # check if our form is valid
        if form.is_valid():

            # try to save the form data to the MySQL database and set the Success message
            try:
                form.save()
                status = "Success!"

            # if there is an exception, set a Failure message
            except Exception as e:
                status = 'Failure: %s (%s)' % (e.args, type(e))

    # else load an empty form
    else:
        form = DatabaseForm()

    # construct the context dictionary to send to the template,
    # i.e. the form elements and status message
    context = {
            'form': form,
            'status': status,
    }

    # send all data to the html template for rendering to the user's browser
    return render(request, 'index.html', context)
