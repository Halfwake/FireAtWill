class Messenger(object):
	game_mode = ""
	items = []
	@staticmethod
	def addItem(item):
		Messenger.items.append(item)
