from github import Github
import os

g = Github(os.environ['github_token'])

def slack_text(json):
    if json['action'] == "created":
        return card_created(json)
    elif json['action'] == "edited":
        return card_created(json)
    elif json['action'] == "moved":
        return  card_moved(json)
    else:
        return "error"

def card_created(json):
    name = json['sender']['login']
    card_name = json['project_card']['note']
    note = get_column(get_project_id(json), json['project_id']['column_id'])
    return "created: " + card_name + "\n" + "by: " + name + "\n" + "note: " + note

def card_moved(json):
    name = json['sender']['login']
    note_changed = get_column(get_project_id(json), json['changes']['column_id']['from'])
    card_name = json['project_card']['note']
    note = get_column(get_project_id(json), json['project_id']['column_id'])

    return "moved: " + card_name + "\n" + "from: " + note_changed + "\n" + "by: " + name + "note: " + note

def card_edited(json):
    name = json['sender']['login']
    card_changed = json['changes']['note']['from']
    card_name = json['project_card']['note']
    note = get_column(get_project_id(json), json['project_id']['column_id'])

    return "edited: " + card_name + "\n" + "from: " + card_changed + "\n" + "by: " + name + "note: " + note
def get_column(project_id, column_id):
    columns = g.get_project(int(project_id)).get_columns()
    for i in columns:
        if i == column_id:
            return i.name
    return "no name"

def get_project_id(json):
    split_str = "https://api.github.com/projects/"

    return json['project_card']['project_url'].split(split_str)[1]