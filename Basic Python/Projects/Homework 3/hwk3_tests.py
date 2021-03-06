3
n|]�  �            	   @   s�   d dl Z d dlmZ d dlmZmZ dd.d/d0gdd� ed�D � d�ddddddddgd�dd1d2d3d4gdd� ed�D � d�d d!d"d#d$gd%d� ed&�D � d�gZd'd(� Zd)d� Z	d*d� Z
d+d� Zd,d � Zed-kr�e�  dS )5�    N)�run)�uniform�randint�same_first_digit�   �   �   �   �#   �"   �   �
   �d   c             C   s(   g | ] }t d d�t d d�t d d�f�qS )r   r   )r   )�.0�x� r   �hwk3_tests.py�
<listcomp>	   s    r   )Ztarget_nameZinputs�get_piece_value�pawn�bishop�knight�rook�queenZkingZforklift�which_season�   �   �	   �   �   c             C   s    g | ]}t d d�t d d�f�qS )r   r   �   )r   )r   r   r   r   r   r      s    �number_to_word�   �    �F   �   c             C   s   g | ]}t d d��qS )r   �c   )r   )r   �_r   r   r   r      s    �   c              C   s$   t jt } tjdd�}t| |� d S )Nz	_tests.py� )�sys�modules�__name__�__file__�replacer   )Z
ref_moduleZstudent_module_namer   r   r   �main   s    
r/   c             C   s0   t | �d t |�d ko.t |�d t |�d kS )Nr   )�str)Znum1Znum2Znum3r   r   r   r   !   s    c             C   s   dddddd�j | �S )Nr   r	   r%   r   )r   r   r   r   r   )�get)�pr   r   r   r   %   s    c             C   sD   d}| d dkr|| d  S d}|| d d
  }|t ||d k� S )N�winter�spring�summer�fallr	   r   r   r   r   r   �   )r3   r4   r5   r6   �r3   r4   r   �r4   r5   r   �r5   r6   r   �r6   r3   r   )r8   r9   r:   r;   )�int)ZmonthZdayZseasonsZdiv_month_infoZ
month_infor   r   r   r   )   s     c             C   s�   ddddddddd	d
d�
}ddddddddd�}ddddddddddd�
}t | �} | |krb||  S t| �d krv||  S | d  d!kr�|| d"  S || d"  d# || d    S )$NZzeroZoneZtwoZthreeZfourZfiveZsixZsevenZeightZnine)
�0�1�2�3�4�5�6�7�8�9ZtwentyZthirtyZfortyZfiftyZsixtyZseventyZeightyZninety)r?   r@   rA   rB   rC   rD   rE   rF   ZtenZelevenZtwelveZthirteenZfourteenZfifteenZsixteenZ	seventeenZeighteenZnineteen)
Z10Z11Z12Z13Z14Z15Z16Z17Z18Z19r   r=   r   � )r0   �len)ZnumberZonesZtensZteensr   r   r   r!   4   s    
�__main__)r   r   r   )r	   r
   r   )r   r   r   )r	   r   )r   r   )r   r   )r   r   )r*   Z
test_toolsr   Zrandomr   r   �rangeZ
test_specsr/   r   r   r   r!   r,   r   r   r   r   �<module>   s&   
$