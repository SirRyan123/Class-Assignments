3
��]�  �               @   s  d dl Z d dlT d dlmZmZ ddddgdd	d
g dddg dd� ed�D � d�ddddddgd�dddddgdd� ed�D � d�dd d!d"d#gd$d� ed�D � d�d%d&d'd(d)d*d+d,d-d.d/d0d1d2d3d4d5gd6d7�gZd8d9� Zd:d� Zd;d� Z	d<d� Z
d=d� Zd>d%� Zed?k�re�  dS )@�    N)�*)�uniform�randint�format_dateZ20190201Z20190202Z20190203Z20190211Z20190212Z20190213Z20190221Z20190222Z20190223c             C   sH   g | ]@}t td d��jd�t tdd��jd� t tdd��jd� �qS )r   i'  �   �   �   �   �   )�strr   �zfill)�.0�_� r   �hwk4_tests.py�
<listcomp>   s   r   �   )�target_name�inputs�is_palindromeZmomzLisa Bonet ate no basilzLager, sir, is regalz#Go hang a salami, I'm a lasagna hogzHey, this isn't a palindrome�number_to_word�   �    �F   �   c             C   s   g | ]}t d d��qS )r   �c   )r   )r   r   r   r   r   r      s    �   �romanize�   �"   �Z   �-   c             C   s   g | ]}t d d��qS )r   r   )r   )r   r   r   r   r   r      s    �standardize_phone_numberz(123) 456-7890z(123)456-7890z(123 456-7890z123) 456-7890z(123) 4567890z(123) 456-789z(123) 456-78900z(123) 4a6-7q90z123-456-7890z123456-7890z123-4567890z123-456-789z123-456-78900z12E-456-789Oz123-4 6-7890zi a fon nmbrT)r   r   Zextra_creditc              C   s$   t jt } tjdd�}t| |� d S )Nz	_tests.py� )�sys�modules�__name__�__file__�replaceZrun)Z
ref_moduleZstudent_module_namer   r   r   �main+   s    
r)   c             C   s�   ddddddddd	d
d�
}ddddddddd�}ddddddddddd�
}t | �} | |krb||  S t| �d krv||  S | d  d!kr�|| d"  S || d"  d# || d    S )$NZzeroZoneZtwoZthreeZfourZfiveZsixZsevenZeightZnine)
�0�1�2�3�4�5�6�7�8�9ZtwentyZthirtyZfortyZfiftyZsixtyZseventyZeightyZninety)r,   r-   r.   r/   r0   r1   r2   r3   ZtenZelevenZtwelveZthirteenZfourteenZfifteenZsixteenZ	seventeenZeighteenZnineteen)
Z10�11�12�13Z14Z15Z16Z17Z18Z19r   r*   r   � )r   �len)�numberZonesZtensZteensr   r   r   r   1   s    
c             C   sT   | j � jdd�jdd�jdd�} tt| �d �}| d|� | | d � d d d� kS )	N�'r#   �,r7   r	   r   r   �����)�lowerr(   �roundr8   )�stringZmidpointr   r   r   r   E   s     c             C   s�   ddddddd�}dddd	d
dddddddg}| dd� t | dd� �| dd �   }}}||d  }|j|�p~|j|d d�}|� d|d dkr�|n|d � |� d|� �S )N�stZndZrdZth)r+   r,   r-   r4   r5   r6   ZJanuaryZFebruaryZMarchZAprilZMayZJuneZJulyZAugustZ	SeptemberZOctoberZNovemberZDecemberr   r   r   r   r7   r*   z, )�int�get)ZdateZordinal_affixesZmonth_namesZyearZ	month_numZdayZmonthZordinal_affixr   r   r   r   K   s    
,c             C   s`   d}|d| d  7 }|d| d  7 }|j dd�j dd�j dd
�}|j dd�j dd�j dd�}|S )Nr#   �X�
   �I�	   ZXCr   �Lr   ZXLZIX�VZIVZ	XXXXXXXXXZXXXXXZXXXXZ	IIIIIIIIIZIIIIIZIIII)r(   )r9   Zrnr   r   r   r   W   s    c             C   s�   | j dd�j dd�j dd�j dd�}|j� o6t|�dks<d S | d dkr�| dd	� d
kr�| d dkr�t| �dkr�| j dd�j dd�j dd�S | d dkr�| d dkr�t| �dkr�| S d S )Nr7   r#   �-�(�)rD   r   r   r   z) rF   �   �   �   r   )r(   �isdigitr8   )Zphone_numberZmaybe_digitsr   r   r   r"   `   s    $�__main__)r$   Z
test_toolsZrandomr   r   �rangeZ
test_specsr)   r   r   r   r   r"   r&   r   r   r   r   �<module>   s:     
	
