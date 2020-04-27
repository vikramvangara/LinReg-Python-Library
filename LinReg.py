w1 = None
w0 = None

x = []
x_test = []

y = []
y_test = []

# Function to Build the Linear Regression Model
def train(file_name,stype='csv'):
    
    global x,y,w1,w0,x_test,y_test

    if stype == 'tab':
        
        #Opening tab seperated values file
        with open(file_name) as inp:
            list_of_rows = list(zip(*(line.strip().split('\t') for line in inp)))
        x = list(list_of_rows[0])
        y = list(list_of_rows[1])

        for i in range(len(x)):
            x[i] = float(x[i])
            y[i] = float(y[i])

    else:
        
        #Opening comma seperated values file
        from csv import reader
        with open(file_name, 'r') as read_obj:
            csv_reader = reader(read_obj)
            list_of_rows = list(csv_reader)
        

        l = len(list_of_rows)

        for i in range(l):
            for j in range(2):
                list_of_rows[i][j] = float(list_of_rows[i][j])
    

        a = []
        b = []

        for i in range(l):
            a.append(list_of_rows[i][0])
            x = a
                
        for i in range(l):
            b.append(list_of_rows[i][1])
            y = b
    
    #Calculating mean of the training data
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
        
    s1,s2 = 0,0
        
    for i in range(len(x)):
        s1 += (x[i] - mean_x) * (y[i] - mean_y)
            
    for i in range(len(x)):
        s2 += (x[i] - mean_x)**2
    
    #Calculating the intercept 'w0' and slope 'w1'
    w1 = s1/s2
    w0 = mean_y - (mean_x*w1)
               
    return [w1,w0]

#Function to get predicted values of Y when X is given
def y_predict(val):
    global w1,w0
    y_pred = []
    if w1 == None or w0 == None:
        print("Model not yet trained!!")
        print("Train the model first!!")
    else:
        
        for i in range(len(val)):
            y_pred.append(round(val[i]*w1 + w0,2))
        
    return y_pred

#Function to get predicted values of X when Y is given
def x_predict(val):
    global w1,w0
    x_pred = []
    if w1 == None or w0 == None:
        print("Model not yet trained!!")
        print("Train the model first!!")
    else:
        for i in range(len(val)):
            x_pred.append(round((val[i]-w0)/w1,2))
            
        return x_pred

#Defining Metrics class to find the error in the data.
class Metrics:
    
    #Mean Absolute error
    def MAE(Y_test,Y_pred):
        diff = 0
        for i in range(len(Y_test)):
            diff += abs(Y_test[i]-Y_pred[i])
        return diff/len(Y_test)
    
    #Mean Squared Error
    def MSE(Y_test,Y_pred):
        diff = 0
        for i in range(len(Y_test)):
            diff += (Y_test[i]-Y_pred[i])**2
        
        return diff/len(Y_test)
    
    #Root Mean Squared Error
    def RMSE(Y_test,Y_pred):
        diff = 0
        for i in range(len(Y_test)):
            diff += (Y_test[i]-Y_pred[i])**2
        
        mae = diff/len(Y_test)
        
        from math import sqrt
        return sqrt(mae)

# Function to get test data in to a list
# to find the errors or to get the predicted data.
def get_list(file_name,stype='csv'):
    
    if stype == 'tab':
        
        #Opening tab seperated values file
        with open(file_name) as inp:
            list_of_rows = list(zip(*(line.strip().split('\t') for line in inp)))
        x = list(list_of_rows[0])
        y = list(list_of_rows[1])

        for i in range(len(x)):
            x[i] = float(x[i])
            y[i] = float(y[i])

    else:
        
        from csv import reader
        with open(file_name, 'r') as read_obj:
            csv_reader = reader(read_obj)
            list_of_rows = list(csv_reader)
        

        l = len(list_of_rows)

        for i in range(l):
            for j in range(2):
                list_of_rows[i][j] = float(list_of_rows[i][j])
    

        a = []
        b = []

        for i in range(l):
            a.append(list_of_rows[i][0])
            x = a
                
        for i in range(l):
            b.append(list_of_rows[i][1])
            y = b
    
    return x,y


