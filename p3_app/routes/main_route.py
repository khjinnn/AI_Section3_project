from flask import Blueprint, render_template, request, redirect
from p3_app.models.flower_model import Flower # route에서 import 해줘야지 테이블이 생성된 것을 감지함..
from p3_app import db
import numpy as np
import pickle

model = pickle.load(open('/Users/moon/Desktop/p3/p3_app/iris.pkl','rb'))


bp = Blueprint('main', __name__)

@bp.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        flower_name = request.form['name']
        flower_att1 = request.form['att1']
        flower_att2 = request.form['att2']
        flower_att3 = request.form['att3']
        flower_att4 = request.form['att4']
        
        new_flower = Flower(name=flower_name, att1=flower_att1, att2=flower_att2, att3=flower_att3, att4=flower_att4) # Todo테이블의 content 항목에 입력된 task_content를 넣어줌

        try:
            db.session.add(new_flower) # 세션이용해서 데이터베이스에 넣을 준비
            db.session.commit() # 데이터베이스에 커밋 
            return redirect('/') # 처음으로 다시 돌아감
        
        except:
            return 'There was an issue adding your task'
    
    else: # POST 가 아닌 그냥 GET 인 경우에는, 데이터베이스에 있는 것들을 나타냄
        things = Flower.query.all() # Todo에 있는 모든 데이터
        return render_template('index.html', things = things) # 데이터를 html 로 넘겨줌

@bp.route('/delete/<int:id>')
def delete(id):
    flowers_to_delete = Flower.query.get_or_404(id)

    try:
        db.session.delete(flowers_to_delete)
        db.session.commit()
        return redirect('/')
    
    except:
        return "There was an issue deleting your task"

@bp.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    thing = Flower.query.get_or_404(id) # id로 task 를 쿼리함

    if request.method=='POST':
        thing.name = request.form['name']
        thing.att1 = request.form['att1']
        thing.att2 = request.form['att2']
        thing.att3 = request.form['att3']
        thing.att4 = request.form['att4']

        try:
            db.session.commit() # 이미 있는 것을 수정하는 것이므로 add 할 필요 없음
            return redirect('/')

        except:
            return "There is an issue updating your task"

    else: 
        return render_template('update.html', thing=thing)

@bp.route('/predict/<int:id>')
def predict(id):
    flowers_to_predict =  Flower.query.get_or_404(id)

    data1 = flowers_to_predict.att1
    data2 = flowers_to_predict.att2
    data3 = flowers_to_predict.att3
    data4 = flowers_to_predict.att4

    array = np.array([[data1, data2, data3, data4]])
    pred = model.predict(array)

    return render_template('predict.html', data=pred)