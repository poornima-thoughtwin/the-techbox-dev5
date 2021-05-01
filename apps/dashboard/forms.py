
from django import forms
from django.views import View
from .models import Employee,Designation, Asset,Category,AssetAssign

class EmployeeForm(forms.ModelForm):  
    
    class Meta:
        model = Employee
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name','id':'name_id'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'email','id':'email_id'}),
            'designation': forms.Select(attrs={'class':'form-control','id':'designation_id'}),
            'phone' : forms.TextInput(attrs={'minlength': 10, 'maxlength': 15, 'required': True, 'type': 'number','class':'form-control','id':'phone_id'}), 
            'address' : forms.TextInput(attrs={'class':'form-control','placeholder':'Address','id':'address_id'}),     
            
        }
        fields = "__all__"
        exclude =('status',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['designation'].queryset = Designation.objects.all()


class AssetForm(forms.ModelForm):  
    
    class Meta:
        model = Asset
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
            # 'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'model_number': forms.TextInput(attrs={'class':'form-control','placeholder':'model_number'}),
            'expire_date' : forms.TextInput(attrs={'minlength': 10, 'maxlength': 15, 'required': True, 'type': 'expire_date','class':'form-control'}), 
            
        }
        fields = "__all__"
        exclude =('status',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['designation'].queryset = Designation.objects.all()


        self.fields['category'].queryset = Category.objects.all()


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
}


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
}


class AssignAssetForm(forms.ModelForm):  
    class Meta:
        model = AssetAssign
        widgets = {
            'employee' : forms.Select(attrs={'class':'form-control'}),
            'asset' : forms.Select(attrs={'class':'form-control'}),
            'expire_date' : forms.TextInput(attrs={'class':'form-control','type': 'date'}),
       }
        fields = "__all__"
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['asset'].queryset =Asset.objects.all()
            self.fields['employee'].queryset = Employee.objects.all()


    # <script>
    #         $(document).on('click', '#delete_record', function (e) {
    #             e.preventDefault();
    #             var obj = $(this); // first store $(this) in obj
    #             var id = $(this).data('id'); // get id of data using this
    #             var my_data = {
    #                 "id": id,
    #                 'csrfmiddlewaretoken': "{{ csrf_token }}",
    #             }
    #             $.ajax({
    #                 type: 'POST',
    #                 url: "{% url 'delete_employee'  %}",
    #                 data: my_data,
    #                 success: function (json) {
    #                     $(obj).closest("tr").remove();
    #                     alert("Employee remove successfully ")
    #                     $('empModal' + id).modal('hide')
    #                     location.reload();
    #                 },
    #             });
    #         });
    #     </script>
     

