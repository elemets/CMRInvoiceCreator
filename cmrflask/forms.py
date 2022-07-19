from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, RadioField, SubmitField, PasswordField, BooleanField, IntegerField, DecimalField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from cmrflask.models import User

class registration_form(FlaskForm):
    username = StringField('Username', 
                          validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()]) 
    confirm_password  = PasswordField('Confirm Password', 
                                      validators=[DataRequired(), EqualTo('password')]) 
    submit = SubmitField('Sign up')
    
    ## validation of username
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please choose another one')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use, please use another one')        


class login_form(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()]) 
    remember = BooleanField('Remember me')
    submit = SubmitField('Log-in')

class cmr_form(FlaskForm):
    sender = TextAreaField('1. Sender (name, address, country)', validators=[DataRequired()])
    consignee = TextAreaField('2. consignee (name, address, country)', validators=[DataRequired()])
    place_of_delivery = TextAreaField('3. Place of delivery (place, country)', validators=[DataRequired()])
    place_of_goods_take_over = TextAreaField('4A. Place of goods take over (place, country)', validators=[DataRequired()])
    date_of_goods_take_over = DateField('4B. Date of goods take over', validators=[DataRequired()])
    annexed_documents = TextAreaField('5. Annexed documents')
    
    ## marks and numbers
    marks_numbers1 = StringField('6. Marks & numbers')
    marks_numbers2 = StringField()
    marks_numbers3 = StringField()       
    marks_numbers4 = StringField()
    marks_numbers5 = StringField()
    marks_numbers6 = StringField()
    marks_numbers7 = StringField()
    marks_numbers8 = StringField()
    
    ## number of packages
    number_packages1 = IntegerField('7. Number of packages')
    number_packages2 = IntegerField()
    number_packages3 = IntegerField()
    number_packages4 = IntegerField()
    number_packages5 = IntegerField()
    number_packages6 = IntegerField()
    number_packages7 = IntegerField()
    number_packages8 = IntegerField()
    
    ## methods of packing 
    method_packing1 = StringField('8. Method of packing')
    method_packing2 = StringField()
    method_packing3 = StringField()
    method_packing4 = StringField()
    method_packing5 = StringField()
    method_packing6 = StringField()
    method_packing7 = StringField()
    method_packing8 = StringField()
    
    ## nature of the goods
    nature_goods1 = StringField('9. Nature of the goods')
    nature_goods2 = StringField()
    nature_goods3 = StringField()
    nature_goods4 = StringField()
    nature_goods5 = StringField()
    nature_goods6 = StringField()
    nature_goods7 = StringField()
    nature_goods8 = StringField()
    
    ## statistical number
    statistical_number1 = IntegerField('10. Statistical number')
    statistical_number2 = IntegerField()
    statistical_number3 = IntegerField()
    statistical_number4 = IntegerField()
    statistical_number5 = IntegerField()
    statistical_number6 = IntegerField()
    statistical_number7 = IntegerField()
    statistical_number8 = IntegerField()
    
    ## gross weights of goods
    gross_weight1 = DecimalField('11. Gross weight KG')
    gross_weight2 = DecimalField()
    gross_weight3 = DecimalField()
    gross_weight4 = DecimalField()
    gross_weight5 = DecimalField()
    gross_weight6 = DecimalField()
    gross_weight7 = DecimalField()
    gross_weight8 = DecimalField()
    total_gross_weight = DecimalField()
    
    ## volume of goods
    volume_goods1  = DecimalField('12. Volume in m³')
    volume_goods2  = DecimalField()
    volume_goods3  = DecimalField()
    volume_goods4  = DecimalField()
    volume_goods5  = DecimalField()
    volume_goods6  = DecimalField()
    volume_goods7  = DecimalField()
    volume_goods8  = DecimalField()
    total_gross_volume = DecimalField()
    
    ## more nature of goods
    classe = StringField('Class')
    number = StringField('Number')
    letter = StringField('Letter')
    ADR = StringField('ADR')
    
    ## Senders instructions
    sender_instructions = TextAreaField("13. Sender's instructions (customs and other formalities)")
    directions_for_freight_payment= TextAreaField("14. Directions for freight payment")
    frieghtpaidradio = RadioField("Freight Paid?", choices=["Freight paid", "Freight to be paid"])
    cash_on_delivery = DecimalField("15. Cash on delivery")
    drop_down_currency_selector_delivery = SelectField("Currency:", choices=["GBP", "EUR", "UAH", "TRY", "SEK", "RUB", "RSD", "RON", "PLN", "NOK", "KRW", "ISK", "HUF", "HRK", "DKK", "CZK", "CHF", "BGN"])
    
    ## carrier name address countr
    
    carrier = TextAreaField('16. Carrier (name, address, country)', validators=[DataRequired()])
    successive_carriers = TextAreaField('17. SuccessiveCarriers (name, address, country)')
    carriers_reservation = TextAreaField("18. Carrier's Reservations and observations")
    special_agreements = TextAreaField("19. Special agreements")
    
    ## To Be Paid By
    # sender
    sender_carriage_charges  = DecimalField("20. Sender carriage charges")
    sender_reductions  = DecimalField()
    sender_balance  = DecimalField()
    sender_supplement_charges  = DecimalField()
    sender_miscellaneous  = DecimalField()
    sender_total  = DecimalField()
    drop_down_currency_selector_sender = SelectField("Currency:", choices=["GBP", "EUR", "UAH", "TRY", "SEK", "RUB", "RSD", "RON", "PLN", "NOK", "KRW", "ISK", "HUF", "HRK", "DKK", "CZK", "CHF", "BGN"])

    # consignee
    consignee_carriage_charges  = DecimalField("Consigneee carriage charges")
    consignee_reductions  = DecimalField()
    consignee_balance  = DecimalField()
    consignee_supplement_charges  = DecimalField()
    consignee_miscellaneous  = DecimalField()
    consignee_total  = DecimalField()
    drop_down_currency_selector_consignee = SelectField("Currency:", choices=["GBP", "EUR", "UAH", "TRY", "SEK", "RUB", "RSD", "RON", "PLN", "NOK", "KRW", "ISK", "HUF", "HRK", "DKK", "CZK", "CHF", "BGN"])

    # established in / on 
    established_in = StringField("21. Established In")
    established_on = DateField("Established On")
    
    # not really sure I need these field as they will always be the same I think
    
    # 24 Tractor license plate
    tractor_license_plate = StringField('24. Tractor License Plate')
    trailer_license_plate = StringField('25. Trailer License Plate')
    
    
    # number of copies selection
    no_copies = SelectField("Number of copies:", choices=["1", "2", "3", "4", "5", "6", "7", "8"])

    # who are the copies for?
    copies_who = RadioField(choices=["Copy for the sender", "Copy for the carrier", "Copy for the consignee"])

    ## Language selection
    primary_language = SelectField("Primary language:", choices=["English", "French"])
    secondary_language = SelectField("Secondary language:", choices=["English", "French"])
    
    submit_preview = SubmitField("Preview")