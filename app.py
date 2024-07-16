'''
Ghassan Qandeel 1212397
Sohaib Badaha 1210472
Hamza Barhosh 1210920
Mohammad Sayyad 1210208
'''
from wtforms import Form
from flask import Flask, render_template,request
from wtforms import StringField, IntegerField, FloatField, SubmitField,SelectField,BooleanField
from wtforms.validators import DataRequired
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="g12g",
    database="pro"
)


cursor = mydb.cursor()




app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'

cursor.execute("select meal_name from meals")
Mname = cursor.fetchall()
cursor.execute("select dessert_name from desserts")
DEname = cursor.fetchall()
cursor.execute("select drink_name from drinks")
DRname = cursor.fetchall()

cursor.execute("select meal_id from meals")
MID = cursor.fetchall()
cursor.execute("select dessert_id from desserts")
DEID = cursor.fetchall()
cursor.execute("select drink_id from drinks")
DRID = cursor.fetchall()

cursor.execute("select price from meals")
Mprice = cursor.fetchall()
cursor.execute("select price from desserts")
DEprice = cursor.fetchall()
cursor.execute("select price from drinks")
DRprice = cursor.fetchall()
'''
# find a new id for order
cursor.execute("select ordar_id from ordar")
temporder = cursor.fetchall()
order_id=[]

for i in range(len(temporder)):
    order_id.append(temporder[i][0])
'''

class MyForm(Form):
    name = StringField('     Name', validators=[DataRequired()])
    ID = IntegerField('      id', validators=[DataRequired()])
    price = FloatField('     price', validators=[DataRequired()])
    submit = SubmitField('Submit')

class OrderForm(Form):
    Mchoices=[]
    DRchoices=[]
    DEchoices=[]
    Mchoices.append(('0', 'No Thing'))
    DEchoices.append(('0', 'No Thing'))
    DRchoices.append(('0', 'No Thing'))

    for i in range(len(Mname)) :
        Mchoices.append((f'{MID[i][0]}',f'{ Mname[i][0] } Price : { Mprice[i][0] }'))

    for i in range(len(DRname)) :
        DRchoices.append((f'{DRID[i][0]}',f'{ DRname[i][0] } Price : { DRprice[i][0] }'))

    for i in range(len(DEname)) :
        DEchoices.append((f'{DEID[i][0]}',f'{ DEname[i][0] } Price : { DEprice[i][0] }'))


    meal = SelectField(u'Choose Meal', choices=Mchoices)
    drink = SelectField(u'Choose drink', choices=DRchoices)
    deserts=SelectField(u'Choose Deserts', choices=DEchoices)
    away_or_table=BooleanField(u'Table ?')

    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/deserts.html', methods=['GET', 'POST'])
def deserts():
    form = MyForm(request.form)
    name = None
    price = None
    ID = None

    if request.method == 'POST' and form.validate():

        name = form.name.data
        price = form.price.data
        ID = form.ID.data
        form.name.data = ''
        form.ID.data = 0
        form.price.data = 0

        query = "INSERT INTO desserts (dessert_id, ordar_did, dessert_name, price) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (ID, None, name, price))
        mydb.commit()
        cursor.execute("select * from desserts")
        for desserts in cursor:
            print(desserts)

    return render_template('deserts.html', form=form, name=name)



@app.route('/drink.html', methods=['GET', 'POST'])
def drink():
    form = MyForm(request.form)
    name = None
    price = None
    ID = None

    if request.method == 'POST' and form.validate():

        name = form.name.data
        price = form.price.data
        ID = form.ID.data
        form.name.data = ''
        form.ID.data = 0
        form.price.data = 0

        query = "INSERT INTO drinks(drink_id, ordar_did, drink_name, price) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (ID, None, name, price))
        mydb.commit()
        cursor.execute("select * from drinks")
        for drinks in cursor:
            print(drinks)

    return render_template('drink.html', form=form, name=name)


@app.route('/food.html', methods=['GET', 'POST'])
def food():
    form = MyForm(request.form)
    name = None
    price = None
    ID =None


    if request.method == 'POST' and form.validate():

            name = form.name.data
            price = form.price.data
            ID = form.ID.data
            form.name.data = ''
            form.ID.data = 0
            form.price.data = 0

            query = "INSERT INTO meals (meal_id, ordar_mid, meal_name, price) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (ID, None, name, price))
            mydb.commit()
            cursor.execute("select * from meals")
            for meal in cursor:
                print(meal)

    return render_template('food.html', form=form, name=name)




@app.route('/menu.html', methods=['GET', 'POST'])
def menu():
    form = OrderForm(request.form)

    if request.method == 'POST' and form.validate():
        away_or_table=form.away_or_table.data
        meal_submit =int( form.meal.data)
        drink_submit = int(form.drink.data)
        desert_submit = int(form.deserts.data)
        form.meal.data=''
        form.drink.data=''
        form.deserts.data=''
        form.away_or_table.data=False


        '''
        cursor.execute("select * from meals")
        for meal in cursor:
            print(meal)
        cursor.execute("select * from drinks")
        for meal in cursor:
            print(meal)
        cursor.execute("select * from desserts")
        for meal in cursor:
            print(meal)
        '''

        if meal_submit !=0 or drink_submit !=0 or desert_submit !=0:
            cursor.execute("select ordar_id from ordar")
            temporder = cursor.fetchall()
            order_id = []

            for i in range(len(temporder)):
                order_id.append(temporder[i][0])

            id_order_inTable = 0;
            total_price = []

            if not order_id:
                id_order_inTable = 1
            else:
                id_order_inTable = max(order_id)
                id_order_inTable = id_order_inTable + 1

            if away_or_table:
                query = "INSERT INTO ordar (ordar_id, cash_idtake ,away_or_table) VALUES (%s, %s,%s)"
                cursor.execute(query, (id_order_inTable, None, 1))
                mydb.commit()
            else:
                query = "INSERT INTO ordar (ordar_id, cash_idtake ,away_or_table) VALUES (%s, %s,%s)"
                cursor.execute(query, (id_order_inTable, None, 0))
                mydb.commit()

            query = "select away_or_table from  ordar  WHERE ordar_id = %s;"
            cursor.execute(query, (id_order_inTable,))
            away_or_table = cursor.fetchall()

            if meal_submit != 0:
                query = "UPDATE meals SET ordar_mid = %s WHERE meal_id = %s"
                cursor.execute(query, (id_order_inTable, meal_submit))
                mydb.commit()  # Commit the transaction
                query = "select meal_id , meal_name , price from  meals m , ordar o WHERE m.ordar_mid = o.ordar_id AND o.ordar_id = %s;"
                cursor.execute(query, (id_order_inTable,))
                meal_order = cursor.fetchall()
                total_price.append(meal_order[0][2])
            else:
                meal_order = [('None','None','None')]

            if desert_submit != 0:
                query = "UPDATE desserts SET ordar_did = %s WHERE dessert_id = %s"
                cursor.execute(query, (id_order_inTable, desert_submit))
                mydb.commit()
                query = "select dessert_id , dessert_name , price from  desserts d , ordar o WHERE d.ordar_did = o.ordar_id AND o.ordar_id = %s;"
                cursor.execute(query, (id_order_inTable,))
                dessert_order = cursor.fetchall()
                total_price.append(dessert_order[0][2])
            else:
                dessert_order = [('None','None','None')]
            if drink_submit != 0:
                query = "UPDATE drinks SET ordar_did = %s WHERE drink_id = %s"
                cursor.execute(query, (id_order_inTable, drink_submit))
                mydb.commit()
                query = "select drink_id , drink_name , price from  drinks d , ordar o WHERE d.ordar_did = o.ordar_id AND o.ordar_id = %s;"
                cursor.execute(query, (id_order_inTable,))
                drink_order = cursor.fetchall()
                total_price.append(drink_order[0][2])
            else:
                drink_order = [('None','None','None')]


            return render_template('Bill.html', order_id=id_order_inTable, meal_order=meal_order,
                                   drink_order=drink_order, dessert_order=dessert_order,
                                   away_or_table=away_or_table[0][0], total_price=sum(total_price))

        else:
         return render_template('Noorder.html')


    return render_template('menu.html',form=form)




@app.route('/Thanks.html')
def Thanks():
    return render_template('Thanks.html')

@app.route('/Contact.html')
def Contact():
    return render_template('Contact.html')

if __name__ == '__main__':
    app.run(debug=True)

