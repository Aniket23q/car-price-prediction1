{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1251e6ec-0879-458d-86d6-0df61360d793",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on all addresses (0.0.0.0)\n",
      " * Running on http://127.0.0.1:8000\n",
      " * Running on http://192.168.129.60:8000\n",
      "Press CTRL+C to quit\n",
      "192.168.129.60 - - [05/Jun/2025 00:25:38] \"GET / HTTP/1.1\" 200 -\n",
      "C:\\Users\\Aniket\\anaconda3\\Lib\\site-packages\\sklearn\\utils\\validation.py:2739: UserWarning: X does not have valid feature names, but RandomForestRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "192.168.129.60 - - [05/Jun/2025 00:26:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "C:\\Users\\Aniket\\anaconda3\\Lib\\site-packages\\sklearn\\utils\\validation.py:2739: UserWarning: X does not have valid feature names, but RandomForestRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "192.168.129.60 - - [05/Jun/2025 00:28:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "C:\\Users\\Aniket\\anaconda3\\Lib\\site-packages\\sklearn\\utils\\validation.py:2739: UserWarning: X does not have valid feature names, but RandomForestRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "192.168.129.60 - - [05/Jun/2025 00:39:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "C:\\Users\\Aniket\\anaconda3\\Lib\\site-packages\\sklearn\\utils\\validation.py:2739: UserWarning: X does not have valid feature names, but RandomForestRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "192.168.129.60 - - [05/Jun/2025 00:40:12] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask  import Flask, render_template, request, jsonify\n",
    "import pickle\n",
    "import numpy as np\n",
    "import sklearn\n",
    "\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "model = pickle.load(open('random_forest_regression_model1.pkl', 'rb'))\n",
    "\n",
    "@app.route('/',methods=['GET'])\n",
    "def Home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "@app.route(\"/predict\", methods=['POST'])\n",
    "def predict():\n",
    "    Fuel_Type_Diesel=0\n",
    "    if request.method == 'POST':\n",
    "        Year = int(request.form['Year'])\n",
    "        Present_Price=float(request.form['Present_Price'])\n",
    "        Kms_Driven=int(request.form['Kms_Driven'])\n",
    "        Kms_Driven2=np.log(Kms_Driven)\n",
    "        Owner=int(request.form['Owner'])\n",
    "        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']\n",
    "        if(Fuel_Type_Petrol=='Petrol'):\n",
    "                Fuel_Type_Petrol=1\n",
    "                Fuel_Type_Diesel=0\n",
    "        else:\n",
    "            Fuel_Type_Petrol=0\n",
    "            Fuel_Type_Diesel=1\n",
    "        Year=2025-Year\n",
    "        Seller_Type_Individual=request.form['Seller_Type_Individual']\n",
    "        if(Seller_Type_Individual=='Individual'):\n",
    "            Seller_Type_Individual=1\n",
    "        else:\n",
    "            Seller_Type_Individual=0\t\n",
    "        Transmission_Mannual=request.form['Transmission_Mannual']\n",
    "        if(Transmission_Mannual=='Mannual'):\n",
    "            Transmission_Mannual=1\n",
    "        else:\n",
    "            Transmission_Mannual=0\n",
    "        prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])\n",
    "        output=round(prediction[0],2)\n",
    "        if output<0:\n",
    "            return render_template('index.html',pred=\"Sorry you cannot sell this car\")\n",
    "        else:\n",
    "            pred = \"You Can Sell The Car at {} lakhs\".format(output)\n",
    "            return render_template('index.html',pred=pred)\n",
    "    else:\n",
    "        return render_template('index.html')\n",
    "\n",
    "if __name__==\"__main__\":\n",
    "    app.run(host='0.0.0.0', port=8000, debug=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "652e6874-b123-47ea-8c88-9a4bbaf6d5c7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
