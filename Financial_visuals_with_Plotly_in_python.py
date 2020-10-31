import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import plotly.express as px
import plotly.graph_objects as go

# Data

start = dt.datetime(2019,1,1)
end = dt.datetime.now()

stocks = web.DataReader(['FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'], 'yahoo', start, end)
stocks_close = pd.DataFrame(web.DataReader(['FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'], 'yahoo', start, end)['Close'])

# 1. Time Series area chart

# a. Basic chart

area_chart = px.area(stocks_close.FB, title = 'FACEBOOK SHARE PRICE (2013-2020)')

area_chart.update_xaxes(title_text = 'Date')
area_chart.update_yaxes(title_text = 'FB Close Price', tickprefix = '$')
area_chart.update_layout(showlegend = False)
area_chart.show()

# b. Customized chart

c_area = px.area(stocks_close.FB, title = 'FACBOOK SHARE PRICE (2013-2020)')

c_area.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

c_area.update_yaxes(title_text = 'FB Close Price', tickprefix = '$')
c_area.update_layout(showlegend = False,
    title = {
        'text': 'FACEBOOK SHARE PRICE (2013-2020)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

c_area.show()

# 2. Candlestick chart

# a. Simple candlestick

candlestick = go.Figure(data = [go.Candlestick(x = stocks.index, 
                                               open = stocks[('Open',    'AMZN')], 
                                               high = stocks[('High',    'AMZN')], 
                                               low = stocks[('Low',    'AMZN')], 
                                               close = stocks[('Close',    'AMZN')])])

candlestick.update_layout(xaxis_rangeslider_visible = False, title = 'AMAZON SHARE PRICE (2013-2020)')
candlestick.update_xaxes(title_text = 'Date')
candlestick.update_yaxes(title_text = 'AMZN Close Price', tickprefix = '$')
candlestick.show()

# b. Customized candlestick

c_candlestick = go.Figure(data = [go.Candlestick(x = stocks.index, 
                                               open = stocks[('Open',    'AMZN')], 
                                               high = stocks[('High',    'AMZN')], 
                                               low = stocks[('Low',    'AMZN')], 
                                               close = stocks[('Close',    'AMZN')])])

c_candlestick.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

c_candlestick.update_layout(
    title = {
        'text': 'AMAZON SHARE PRICE (2013-2020)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
c_candlestick.update_yaxes(title_text = 'AMZN Close Price', tickprefix = '$')
c_candlestick.show()

# 3. OHLC chart

# a. Simple OHLC chart

ohlc = go.Figure(data = [go.Ohlc(x = stocks.index, 
                                               open = stocks[('Open',    'AAPL')], 
                                               high = stocks[('High',    'AAPL')], 
                                               low = stocks[('Low',    'AAPL')], 
                                               close = stocks[('Close',    'AAPL')])])

ohlc.update_layout(xaxis_rangeslider_visible = False, title = 'APPLE SHARE PRICE (2013-2020)')
ohlc.update_xaxes(title_text = 'Date')
ohlc.update_yaxes(title_text = 'AAPL Close Price', tickprefix = '$')
ohlc.show()

# b. Customized OHLC

c_ohlc = go.Figure(data = [go.Ohlc(x = stocks.index, 
                                               open = stocks[('Open',    'AAPL')], 
                                               high = stocks[('High',    'AAPL')], 
                                               low = stocks[('Low',    'AAPL')], 
                                               close = stocks[('Close',    'AAPL')])])

c_ohlc.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

c_ohlc.update_layout(
    title = {
        'text': 'APPLE SHARE PRICE (2013-2020)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
c_ohlc.update_yaxes(title_text = 'AAPL Close Price', tickprefix = '$')
c_ohlc.show()

# 4. Bullet chart

# a. Basic bullet chart

bullet_chart = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet", 'axis': {'range': [None, 600]}},
    value = int(stocks_close['NFLX'].tail(1)),
    delta = {'reference': int(stocks_close['NFLX'].tail(2)[0])},
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text':"<b>NETFLIX<br>STOCK<br>PRICE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 'font': {"size": 12}}))
bullet_chart.update_layout(height = 250)
bullet_chart.show()

# b. Customized bullet chart

c_bullet = go.Figure()

c_bullet.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = int(stocks_close['NFLX'].tail(1)),
    delta = {'reference': int(stocks_close['NFLX'].tail(2)[0])},
    domain = {'x': [0.25, 1], 'y': [0.08, 0.25]},
    title = {'text':"<b>NETFLIX DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 'font': {"size": 14}},    
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 550]},
        'threshold': {
            'line': {'color': "Red", 'width': 2},
            'thickness': 0.75,
            'value': 505},
        'steps': [
            {'range': [0, 350], 'color': "gray"},
            {'range': [350, 550], 'color': "lightgray"}],
        'bar': {'color': 'black'}}))

c_bullet.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = int(stocks_close['GOOGL'].tail(1)),
    delta = {'reference': int(stocks_close['GOOGL'].tail(2)[0])},
    domain = {'x': [0.25, 1], 'y': [0.4, 0.6]},
    title = {'text':"<b>GOOGLE DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 'font': {"size": 14}},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 1800]},
        'threshold': {
            'line': {'color': "red", 'width': 2},
            'thickness': 0.75,
            'value': 1681},
        'steps': [
            {'range': [0, 1300], 'color': "gray"},
            {'range': [1300, 1800], 'color': "lightgray"}],
        'bar': {'color': 'black'}}))

c_bullet.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = int(stocks_close['MSFT'].tail(1)),
    delta = {'reference': int(stocks_close['MSFT'].tail(2)[0])},
    domain = {'x': [0.25, 1], 'y': [0.7, 0.9]},
    title = {'text':"<b>MICROSOFT DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 'font': {"size": 14}},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 250]},
        'threshold': {
            'line': {'color': "red", 'width': 2},
            'thickness': 0.75,
            'value': 208},
        'steps': [
            {'range': [0, 150], 'color': "gray"},
            {'range': [150, 250], 'color': "lightgray"}],
        'bar': {'color': "black"}}))

c_bullet.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})
c_bullet.show()

# 5. Gauge charts

gauge = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = int(stocks_close['FB'].tail(1)),
    mode = "gauge+number+delta",
    title = {'text':"<b>FACEBOOK DAY RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 'font': {"size": 20}},
    delta = {'reference': int(stocks_close['FB'].tail(2)[0])},
    gauge = {'axis': {'range': [None, 300]},
             'steps' : [
                 {'range': [0, 200], 'color': "lightgray"},
                 {'range': [200, 300], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 276}}))
gauge.show()
