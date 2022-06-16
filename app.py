import os
from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, FloatField
from flask_fontawesome import FontAwesome


app = Flask(__name__)
fa = FontAwesome(app)
app.config["SECRET_KEY"] = "AComplicat3dText."

CONCRETE_CLASSES = ["C12/15", "C16/20", "C20/25", "C25/30", 
                "C25/30", "C30/37", "C35/45", "C40/50", "C45/55"]


class Rect_CS:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.area = self.width * self.height   
        

class RC_Rect_CS(Rect_CS):
    def __init__(self, width, height, 
                 concrete, reinforcement, concrete_cover):
        super().__init__(width, height)
        self.concrete = concrete
        self.reinforcement = reinforcement
        self.concrete_cover = concrete_cover
 
"""    
class_Reinforcing_Steel:
    def __init__(self, steel_class, E, gamma):
"""       

class Concrete:
    
    def __init__(self, strength_class, 
                 gamma, alpha_ccpl=1, alpha_ctpl=1, etta=1, ultimate_strain=3.5):
        
        self.strength_class = strength_class
        self.gamma = gamma
        self.alpha_ccpl = alpha_ccpl
        self.alpha_ctpl = alpha_ctpl
        self.ultimate_strain = ultimate_strain       
        self.strength_class = strength_class.replace(" ", "")
        
            
        if self.strength_class == "C12/15":
            
            self.f_ck = 12
            self.f_cm = 20
            self.f_ctm = 1.6
            self.f_ctk005 = 1.1
            self.f_ctk095 = 2
            self.E_Modul = 27000
                        
                 
        elif self.strength_class == "C16/20":
            
            self.f_ck = 16
            self.f_cm = 24
            self.f_ctm = 1.9
            self.f_ctk005 = 1.3
            self.f_ctk095 = 2.5
            self.E_Modul = 29000     
            
            
        elif self.strength_class == "C20/25":
            
            self.f_ck = 20
            self.f_cm = 28
            self.f_ctm = 2.2
            self.f_ctk005 = 1.5
            self.f_ctk095 = 2.9
            self.E_Modul = 30000 
            
            
        elif self.strength_class == "C25/30":
            
            self.f_ck = 25
            self.f_cm = 33
            self.f_ctm = 2.6
            self.f_ctk005 = 1.8
            self.f_ctk095 = 3.3
            self.E_Modul = 31000     
            
            
        elif self.strength_class == "C30/37":
            
            self.f_ck = 30
            self.f_cm = 38
            self.f_ctm = 2.9
            self.f_ctk005 = 2
            self.f_ctk095 = 3.8
            self.E_Modul = 32000
            
 
        elif self.strength_class == "C35/45":
            
            self.f_ck = 35
            self.f_cm = 43
            self.f_ctm = 3.2
            self.f_ctk005 = 2.2
            self.f_ctk095 = 4.2
            self.E_Modul = 34000
            
            
        elif self.strength_class == "C40/50":
            
            self.f_ck = 40
            self.f_cm = 48
            self.f_ctm = 3.5
            self.f_ctk005 = 2.5
            self.f_ctk095 = 4.6
            self.E_Modul = 35000


        elif self.strength_class == "C45/55":
            
            self.f_ck = 45
            self.f_cm = 53
            self.f_ctm = 3.8
            self.f_ctk005 = 2.7
            self.f_ctk095 = 4.9
            self.E_Modul = 36000
            

        elif self.strength_class == "C50/60":
            
            self.f_ck = 50
            self.f_cm = 58
            self.f_ctm = 4.1
            self.f_ctk005 = 2.9
            self.f_ctk095 = 5.3
            self.E_Modul = 37000
            
            
        elif self.strength_class == "C55/65":
            
            self.f_ck = 55
            self.f_cm = 63
            self.f_ctm = 4.2
            self.f_ctk005 = 3.0
            self.f_ctk095 = 5.5
            self.E_Modul = 38000


        elif self.strength_class == 60:
            
            self.f_ck = 60
            self.f_cm = 68
            self.f_ctm = 4.4
            self.f_ctk005 = 3.1
            self.f_ctk095 = 5.7
            self.E_Modul = 39000            
            
 
        elif self.strength_class == 70:
            
            self.f_ck = 70
            self.f_cm = 78
            self.f_ctm = 4.6
            self.f_ctk005 = 3.2
            self.f_ctk095 = 6.0
            self.E_Modul = 41000   
            
            
        elif self.strength_class == 80:
            
            self.f_ck = 80
            self.f_cm = 88
            self.f_ctm = 4.8
            self.f_ctk005 = 3.4
            self.f_ctk095 = 6.3
            self.E_Modul = 42000
            
            
        elif self.strength_class == 90:
            
            self.f_ck = 90
            self.f_cm = 98
            self.f_ctm = 5
            self.f_ctk005 = 3.5
            self.f_ctk095 = 6.6
            self.E_Modul = 44000
        


class ConcreteForm(FlaskForm):
   
    def validate_concrete_class(form,field):    
        if field.data.replace(" ", "") not in CONCRETE_CLASSES:
            field.data = "C20/25"
            raise ValidationError("Please provide the concrete class in form \
                                  as in EC2 (for example C20/25)")
           
    def validate_alfa_ccpl(form,field):
        if field.data != 1:
            raise ValidationError("The only value I want is 1")
          
    def validate_alfa_ctpl(form, field):
        if field.data != 1:
            raise ValidationError("The only value I want is 1")
           
    def validate_ultimate_strain(form,field):
        if field.data != 3.5:
            raise ValidationError("The only value I want is 3.5")
           
    def validate_etta(form,field):
        if field.data != 1:
            raise ValidationError("The only value I want is 1")

    def validate_partial_safety_factor(form,field):
        if field.data not in [1.4, 1.5]:
            raise ValidationError("Only 1.4 or 1.5 possible")
           
    
    strength_class = StringField("Please provide the concrete class",
                                 render_kw={"class":"string_class"},  
                                 validators = [DataRequired("Field cannot be empty"),
                                               validate_concrete_class], 
                                 default="C20/25")
    alpha_ccpl = IntegerField(validators=[validate_alfa_ccpl])
    alpha_ctpl = IntegerField(validators=[validate_alfa_ctpl])
    ultimate_strain = FloatField(validators=[validate_ultimate_strain])
    etta = IntegerField(validators=[validate_etta])
    gamma = FloatField(validators=[validate_partial_safety_factor])
    
    
    
    
    

@app.route('/', methods=["POST", "GET"])
def index():
    form = ConcreteForm(csrf_enabled = True)
    
    if form.validate_on_submit(): 
        concrete = Concrete(
            strength_class = form.strength_class.data, 
            gamma = form.gamma.data,
            alpha_ccpl = form.alpha_ccpl.data,
            alpha_ctpl = form.alpha_ctpl.data,
            etta = form.etta.data, 
            ultimate_strain = form.ultimate_strain.data)
            
            
            
        return render_template("result.html", concrete_class=concrete)
    #form.form_errors.clear
    #form = ConcreteForm(csrf_enabled=True)
    return render_template("index.html", form=form) #proba zamiast render_template
    
    
@app.route("/result.html", methods=["POST", "GET"])
def result():
    return render_template("result.html")


if __name__ == '__main__':
    app.run(debug=False,port=os.getenv('PORT',5000))



