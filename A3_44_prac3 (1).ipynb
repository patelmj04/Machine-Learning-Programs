{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f2b7a0a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4041319c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('enjoysport.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b481ba2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sky</th>\n",
       "      <th>AirTemp</th>\n",
       "      <th>Humidity</th>\n",
       "      <th>Wind</th>\n",
       "      <th>Water</th>\n",
       "      <th>Forecast</th>\n",
       "      <th>EnjoySport</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Sunny</td>\n",
       "      <td>Warm</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Strong</td>\n",
       "      <td>Warm</td>\n",
       "      <td>Same</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Sunny</td>\n",
       "      <td>Warm</td>\n",
       "      <td>High</td>\n",
       "      <td>Strong</td>\n",
       "      <td>Warm</td>\n",
       "      <td>Same</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Rainy</td>\n",
       "      <td>Cold</td>\n",
       "      <td>High</td>\n",
       "      <td>Strong</td>\n",
       "      <td>Warm</td>\n",
       "      <td>Change</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Sunny</td>\n",
       "      <td>Warm</td>\n",
       "      <td>High</td>\n",
       "      <td>Strong</td>\n",
       "      <td>Cool</td>\n",
       "      <td>Change</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Sky AirTemp Humidity    Wind Water Forecast  EnjoySport\n",
       "0  Sunny    Warm   Normal  Strong  Warm     Same           1\n",
       "1  Sunny    Warm     High  Strong  Warm     Same           1\n",
       "2  Rainy    Cold     High  Strong  Warm   Change           0\n",
       "3  Sunny    Warm     High  Strong  Cool   Change           1"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "43e2401b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Specific Hypothesis: ['Sunny' 'Warm' 'Normal' 'Strong' 'Warm' 'Same']\n",
      "General Hypothesis: [['?', '?', 'Normal', '?', '?', '?'], ['?', '?', '?', '?', 'Warm', '?'], ['?', '?', '?', '?', '?', 'Same']]\n"
     ]
    }
   ],
   "source": [
    "def candidate_elimination(df):\n",
    "    specific_h = df.iloc[0][:-1].values\n",
    "    general_h = [[\"?\" for _ in range(len(specific_h))] for _ in range(len(specific_h))]\n",
    "\n",
    "    for index, row in df.iterrows():\n",
    "        if row.iloc[-1] == \"yes\":\n",
    "            for i in range(len(specific_h)):\n",
    "                if row.iloc[i] != specific_h[i]:\n",
    "                    specific_h[i] = \"?\"\n",
    "                    general_h[i][i] = \"?\"\n",
    "\n",
    "        else:\n",
    "            for i in range(len(specific_h)):\n",
    "                if row.iloc[i] != specific_h[i]:\n",
    "                    general_h[i][i] = specific_h[i]\n",
    "                else:\n",
    "                    general_h[i][i] = \"?\"\n",
    "            \n",
    "        empty = 0\n",
    "    for i in range(len(general_h)):\n",
    "      if (general_h[i] == ['?', '?', '?', '?', '?', '?']):\n",
    "        empty +=1\n",
    "\n",
    "    for i in range(empty):\n",
    "      general_h.remove(['?', '?', '?', '?', '?', '?'])\n",
    "    return specific_h,general_h\n",
    "\n",
    "specific_h, general_h = candidate_elimination(df)\n",
    "print(\"Specific Hypothesis:\", specific_h)\n",
    "print(\"General Hypothesis:\", general_h)\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "883d0aee",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f283df49",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
