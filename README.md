*��� �������-��������� 4�. �� ���� �������� ������ � �������� ������: https://t.me/AnnLinnden*
# ��� ������ ������?
�������� ������ ������� ���� � �������� ���������, ������� ������������ ����� ������������ ���������� �������. 
������������ ������������� �� ����, ���������� �������� ������� � �������� ������� �������������� ���� �������.
������� � ���� ���� ����������� � Telegram Stars, ��������� ���� ���� � �������� ��������. ���� ��� ����� ������������
���� ��� ������� ���������� ���������, ���������� ��������� ������� � Telegram � [�������� bot.send_invoice](timing/payments.py): 
������� ������ currency � provider_token. ���� �� �������� �������� �������, ������ ������ �� �����.
# ��� �������� � ��������?
## �������� ����������� ���� .env � �������� �����
��������� ���, ������:

* TOKEN=����� ������ ����
* ADMINS=������ id ������������� ��������, ������� ����� ������ ���� � �������
* HOST_REDIS=���� �����, ������� �� �����������
* PORT_REDIS=���� �����
* USERNAME_REDIS=�������� �����
* PASSWORD_REDIS=������ �����, ������� �� ����������

## �������� ���� config.py
� ��� ����� ������� � ��������������� ������� ��������, ��������, ���� ������ ��������, ��������-������ ��� �������,
� ����� ������ ������ � ���� ����. �������� ��������: �� �������� ��������, ������� paysupport ������ ���� �����������!
�����: ��� �������� ���, ����� ��������� ������������ ������ ������ ����. ���� �� ������ ��� ��������, 
[�������� time_functions.py � ����� timing](timing/time_functions.py) � �������� ������ 20.

## �������� ���� messages.py � ����� handlers
� ��� �� ������� �������� - �������� �� �� ����������� ������. � ������ ������� message_day_� ����� ��������
�������� �������������� ��������� (������� �����, ���� � ��.) - � ���� ������� ����� ������� ������� ���������, 
������� ��� �����.
���� �� ���������� ��������� ������� �����, ���������������� ������ 18 (self.money_refund_message) � �������� ���������, 
� ����� �������� ��������������� ������� [� user_handlers.py � ��� �� �����](handlers/user_handlers.py).

## ��� ������, ���� ����� ������/������ ������� ���������?
[� ����� messages.py](handlers/messages.py) �������� ��� ������� ������� async def message_day_�. 
����� ��������� ������� message_chain.
�� ��������� ���������� ����.