import wx

# Braille input based on NVDA PC Keyboard Braille Input addon
#---------------------------------------------------------------------------

DOT1 = 1 << 0
DOT2 = 1 << 1
DOT3 = 1 << 2
DOT4 = 1 << 3
DOT5 = 1 << 4
DOT6 = 1 << 5
DOT7 = 1 << 6
DOT8 = 1 << 7

VKCODES_TO_DOTS = {
	70: DOT1, # f
	68: DOT2, # d
	83: DOT3, # s
	74: DOT4, # j
	75: DOT5, # k
	76: DOT6, # l
	65: DOT7, # a
	186: DOT8, # ;
	82: DOT1, # r
	69: DOT2, # e
	87: DOT3, # w
	85: DOT4, # u
	73: DOT5, # i
	79: DOT6, # o
	81: DOT7, # q
	80: DOT8, # p
	32: 0, # space,
}

class BrailleTextCtrl(wx.TextCtrl):
	def __init__(self, *args, **kwargs):
		wx.TextCtrl.__init__(self, *args, **kwargs)
		self._trappedKeys = set()
		self._gesture = None
		
		self.Bind(wx.EVT_KEY_DOWN, self.EvtKeyDown, self)
		self.Bind(wx.EVT_KEY_UP, self.EvtKeyUp, self)

	def EvtKeyDown(self, event):
		#TODO: if control or alt key is pressed then evnt.Skip()
		vkCode = event.GetKeyCode()
		dot = VKCODES_TO_DOTS.get(vkCode)
		if dot is None:
			event.Skip()
			return
		self._trappedKeys.add(vkCode)
		if dot == 0:
			self._gesture = 0
		elif self._gesture:
			self._gesture |= dot
		else:
			self._gesture = dot
		return False

	def EvtKeyUp(self, event):
		vkCode = event.GetKeyCode()
		if vkCode not in self._trappedKeys:
			event.Skip()
			return
		self._trappedKeys.discard(vkCode)
		if not self._trappedKeys and self._gesture is not None:
			text = unichr(self._gesture | 0x2800)
			self.WriteText(text)
			self.SetDefaultStyle(wx.TextAttr(wx.RED))
			self._gesture = None
		return False