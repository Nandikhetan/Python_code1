from django import forms


class StudentInfo2(forms.Form):
    Rollno = forms.IntegerField()
    Name = forms.CharField()
    Class = forms.CharField()
    School = forms.CharField()
    Mobile = forms.IntegerField()
    Address = forms.CharField()
    Mathsmarks = forms.IntegerField()
    Physicsmarks = forms.IntegerField()
    Chemistrymarks = forms.IntegerField()
    Biologymarks = forms.IntegerField()
    Englishmarks = forms.IntegerField()

    def student(self):
        pass
