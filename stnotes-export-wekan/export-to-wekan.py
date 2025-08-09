import os
import time
from wekan import WekanClient

TXT_DIR = r'G:\standardnotes'


if __name__ == '__main__':
    wekan = WekanClient(
        base_url='http://localhost:2000',
        username='user',
        password='pass')
    
    board = wekan.list_boards(regex_filter='Personal')[0]
    swimlane = board.list_swimlanes()[0]
    lists = board.get_lists(regex_filter='Imported')[0]
    lists.swimlane_id = swimlane.id

    for filename in os.listdir(TXT_DIR):
        if filename.lower().endswith('.txt'):
            filepath = os.path.join(TXT_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            lists.create_card(title=filename,
                              description=content)
            print('Arquivo ', filename, ' importado com sucesso.')

