from flask import Flask, render_template, request, redirect, url_for, session

import time

app = Flask(__name__)



# 出席番号と時間を格納する変数
attendance_number = ""
start_time = None
end_time = None


# 出席番号入力画面
@app.route('/', methods=['GET', 'POST'])
def index():
    global attendance_number
    if request.method == 'POST':
        attendance_number = request.form['attendance_number']
        # ここでinstructionsにリダイレクトする
        return redirect(url_for('instructions', attendance_number=attendance_number))
    return render_template('index.html')


# 説明画面
@app.route('/instructions', methods=['GET', 'POST'])
def instructions():
    global attendance_number 

    

    if request.method == 'POST':
        attendance_number = request.form.get('attendance_number', '')

      

        # ボタンがクリックされたときだけリダイレクト
        return redirect(url_for('countdown'))

    return render_template('instructions.html', attendance_number=attendance_number)

# カウントダウン画面
@app.route('/countdown', methods=['GET', 'POST'])
def countdown():
    global attendance_number
    if request.method == 'POST':
        attendance_number = request.form.get('attendance_number', '')
        # リダイレクト先のURLを指定し、リダイレクト
        return redirect(url_for('test'))

    
    return render_template('countdown.html', attendance_number=attendance_number)

# テスト画面
@app.route('/test', methods=['GET', 'POST'])
def test():
    global start_time, attendance_number ,end_time
    
    if request.method == 'GET':
        start_time = time.time()  # 新しい試験が始まるたびに start_time を初期化
        # end_time = None  # 新しい試験が始まるたびに end_time を初期化
        # GET リクエストの場合、test.html を表示
        return render_template('test.html', attendance_number=attendance_number, is_middle_school=True)
        
    elif request.method == 'POST':
        
       

        # timeTaken1 = request.form.get('timeTaken1', '')
    
        # timeTaken = request.form.get('timeTaken', '')
        

        # if request.form.get('choice') == '自分':
        #     end_time = time.time()
        # else:
        #     # 不正解の場合の処理
        #     pass

        # end_time_from_client = request.form.get('end_time')
        # app.logger.info(f'end_time_from_client: {end_time_from_client}')

        # if request.form.get('choice') == '自分':
        #     if end_time_from_client is not None:
        #         end_time = float(end_time_from_client)
        # else:
        #     # 不正解の場合の処理
        #     pass
        
        # app.logger.info(f'start_time: {start_time}, end_time: {end_time}')
        
    # app.logger.info(f'Attendance Number in /test: {attendance_number}')

# セッションにデータを保存
        # session['start_time'] = start_time
        # session['end_time'] = end_time
        # session['timeTaken'] = timeTaken  # 追加

        # timeTaken = round(end_time - start_time, 2)
     return redirect(url_for('result', attendance_number=attendance_number))
    # return render_template('test.html', attendance_number=attendance_number, is_middle_school=True)
    #     return render_template('test.html' , attendance_number=attendance_number)
    # return redirect(url_for('result'))

# 結果表示画面
@app.route('/result')
def result():
    global attendance_number 
    timeTaken1 = request.form.get('timeTaken1', '')
    app.logger.info(f'timeTaken1: {timeTaken1}')

    # セッションからデータを取得
    # start_time = session.get('start_time')
    # end_time = session.get('end_time')
    # timeTaken = session.get('timeTaken')  # 追加
    
    
    


    
        
    return render_template('result.html', timeTaken1=timeTaken1 ,attendance_number=attendance_number)
    
    # timeTaken = round(end_time - start_time, 2)
# app.logger.info(f'timeTaken1 in /result: {timeTaken1}')
   
    # return render_template('result.html', attendance_number=attendance_number, timeTaken=timeTaken)
# if __name__ == '__main__':
#  app.run(debug=True)
