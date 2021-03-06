3
>�\]z  �               @   s�   d dl Z d dlmZ d dlmZmZmZ ddddgdd	� ed
�D � d�dd&d'd(d)gdd	� ed�D � dd�dd*d+d,gdd	� ed
�D � d�ddd	� d-D �d�gZdd � Z	d!d� Z
d"d� Zd#d� Zd$d� Zed%k� r�e	�  dS ).�    N)�run)�uniform�randint�choice�seconds_to_dhmsi�� �   i�� c             C   s   g | ]}t d d��qS )i  i@B )r   )�.0�x� r
   �hwk2_tests.py�
<listcomp>   s   r   �   )�target_name�inputs�metricifier�d   �   �   �   c             C   s$   g | ]}t d d�ttd d��f�qS )r   r   �   )r   r   �range)r   r	   r
   r
   r   r      s    �   g{�G�z�?)r   r   Z	tolerance�is_valid_triangle�   �   r   c             C   s(   g | ] }t d d�t d d�t d d�f�qS )r   �
   �   )r   )r   r	   r
   r
   r   r      s    �find_rps_outcomec             C   s   g | ]}dD ]}||f�qqS )�rock�paper�scissors)r   r   r    r
   )r   r	   �yr
   r
   r   r      s    r   r   r    c              C   s$   t jt } tjdd�}t| |� d S )Nz	_tests.py� )�sys�modules�__name__�__file__�replacer   )Z
ref_moduleZstudent_module_namer
   r
   r   �main   s    
r(   c             C   s0   g }x"dD ]}|j | | � | |; } q
W t|�S )N�Q �  �<   r   )r)   r*   r+   r   )�append�tuple)Zseconds�resultZfactorr
   r
   r   r   $   s
    
c             C   s(   dd� dd� dd� dd� g}|| | �S )Nc             S   s   t | d d d�S )N�    �   �	   r   gr�q��?)�round)�fr
   r
   r   �<lambda>-   s    zmetricifier.<locals>.<lambda>c             S   s   t | d d�S )Ng����ׁ�?r   )r2   )Zfeetr
   r
   r   r4   .   s    c             S   s   t | d d�S )Ng���j��?r   )r2   )Zpoundsr
   r
   r   r4   /   s    c             S   s   t | d d�S )Ng�#W��H@r   )r2   )Zgallonsr
   r
   r   r4   0   s    r
   )Zquantity�flagZconversionsr
   r
   r   r   ,   s
    
c             C   s6   t | ||f�}x"| ||fD ]}||| krdS qW dS )NFT)�sum)Zside1Zside2Zside3Z	all_sidesZsider
   r
   r   r   4   s
     c             C   s0   dddd�}| |krdS ||  |kr(dS dS d S )Nr    r   r   )r   r   r    zTie gamezPlayer 1 winszPlayer 2 winsr
   )Z	p1_choiceZ	p2_choiceZwinnersr
   r
   r   r   ;   s    �__main__)r   r   )r   r   )r   r   )r   r   )r   r   r   )r   r   r   )r   r   r   )r   r   r    )r#   Z
test_toolsr   Zrandomr   r   r   r   Z
test_specsr(   r   r   r   r   r%   r
   r
   r
   r   �<module>   s*   


