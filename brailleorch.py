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

class BrailleOrchFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title="BrailleOrch")
		self._trappedKeys = set()
		self._gesture = None
		
		menuBar = wx.MenuBar()

		fileMenu = wx.Menu()
		fileMenu.Append(wx.ID_NEW, "&New", "Create a new BrailleOrch score")
		fileMenu.Append(wx.ID_OPEN, "&Open...", "Open an existing BrailleOrch score")
		fileMenu.Append(101, "&Open recent...", "Open a recently opened score")
		fileMenu.Append(wx.ID_SAVE, "&Save", "Saves the current score")
		fileMenu.Append(wx.ID_SAVEAS, "Save &as...", "Save the current score to a new file")
		
		versioning = wx.Menu()
		versioning.Append(112, "&Save Version...", "Save a copy of the current score in a new file")
		versioning.Append(122, "&Open Version...", "Open a previously saved version of the current score")
		fileMenu.AppendMenu(102, "&Versioning...", versioning)

		fileMenu.Append(103, "Set copy &protection", "Apply copy protection to current score")
		fileMenu.Append(104, "Make final document", "Remove temporary metadata")
		fileMenu.Append(wx.ID_CLOSE_ALL, "Close &All", "Close all open scores")
		fileMenu.Append(105, "Import...", "Import a score from a different format")
		fileMenu.Append(106, "Export...", "Export current score to a different format")
		fileMenu.Append(wx.ID_PAGE_SETUP, "&Page setup...", "Open the Page Setup dialog box")
		fileMenu.Append(107, "Emboss...", "Emboss the current score")
		fileMenu.AppendSeparator()
		fileMenu.Append(wx.ID_EXIT, "E&xit", "Exit BrailleOrch")
		menuBar.Append(fileMenu, "&File")

		editMenu = wx.Menu()
		editMenu.Append(wx.ID_UNDO, "&Undo", "Undo previous command")
		editMenu.Append(wx.ID_REDO, "&Redo", "Redo an undone command")
		editMenu.Append(201, "Undo &history", "Open the Undo History dialog box")
		editMenu.Append(wx.ID_SELECTALL, "Select &all", "Select the entire score")

		selectionMenu = wx.Menu()
		selectionMenu.Append(202, "Set begin of selection block (F5)")
		selectionMenu.Append(203, "Set end of selection block (F6)")
		selectionMenu.Append(204, "Set from begin to current location (F7)")
		selectionMenu.Append(205, "Select from current location to end (F8)")
		selectionMenu.Append(206, "Select line (F9)")
		selectionMenu.Append(207, "Select part (F9)")
		selectionMenu.Append(208, "Select staff (F10)")
		selectionMenu.Append(209, "Select system (F12)")
		selectionMenu.Append(210, "Remove selection (F4)")
		editMenu.AppendMenu(211, "Special selection", selectionMenu)

		editMenu.Append(wx.ID_CUT, "Cu&t")
		editMenu.Append(wx.ID_COPY, "&Copy")
		editMenu.Append(wx.ID_PASTE, "&Paste")
		editMenu.Append(wx.ID_DELETE, "&Delete")

		editMenu.Append(212, "Cut part")
		editMenu.Append(213, "Copy part")
		editMenu.Append(214, "Paste part")
		editMenu.Append(215, "Delete part")

		editMenu.Append(216, "Search or replace")
		menuBar.Append(editMenu, "&Edit")

		viewMenu = wx.Menu()
		viewMenu.Append(301, "Zoom &in")
		viewMenu.Append(302, "Zoom &out")
		viewMenu.AppendSeparator()
		viewMenu.Append(303, "&Toolbar")
		viewMenu.AppendSeparator()
		viewMenu.AppendRadioItem(304, "&Black on white")
		viewMenu.Check(304, True)
		viewMenu.AppendRadioItem(305, "&White on black")
		viewMenu.AppendRadioItem(306, "&Blue on black")
		viewMenu.AppendRadioItem(307, "&Green on black")
		menuBar.Append(viewMenu, "&View")

		navigationMenu = wx.Menu()
		nextMenu = wx.Menu()
		nextMenu.Append(401, "Note (tab)")
		nextMenu.Append(403, "Beat (alt+right)")
		nextMenu.Append(405, "Measure (ctrl+right)")
		nextMenu.Append(407, "Voice (win+right)")
		nextMenu.Append(409, "Part in measure (ctrl+down)")
		nextMenu.Append(411, "Print line (alt+down)")
		nextMenu.Append(413, "Braille system (win+down)")
		nextMenu.Append(415, "Print system (ctrl+win+down)")
		nextMenu.Append(417, "Braille page (pgdn)")
		nextMenu.Append(419, "Print page (ctrl+pgdn)")
		navigationMenu.AppendMenu(450, "Next", nextMenu)
		previousMenu = wx.Menu()
		previousMenu.Append(402, "Note (shift+tab)")
		previousMenu.Append(404, "Beat (alt+left)")
		previousMenu.Append(406, "Measure (ctrl+left)")
		previousMenu.Append(408, "Voice (win+left)")
		previousMenu.Append(410, "Part in measure (ctrl+up)")
		previousMenu.Append(412, "Print line (alt+up)")
		previousMenu.Append(414, "Braille system (win+up)")
		previousMenu.Append(416, "Print system (ctrl+win+up)")
		previousMenu.Append(418, "Braille page (pgup)")
		previousMenu.Append(420, "Print page (ctrl+pgup)")
		navigationMenu.AppendMenu(499, "Previous", previousMenu)
		startMenu = wx.Menu()
		startMenu.Append(421, "Braille page (home)")
		startMenu.Append(423, "System (alt+home)")
		startMenu.Append(425, "File (ctrl+home)")
		navigationMenu.AppendMenu(475, "Start of", startMenu)
		endMenu = wx.Menu()
		endMenu.Append(422, "Braille page (end)")
		endMenu.Append(424, "System (alt+end)")
		endMenu.Append(426, "File (ctrl+end)")
		navigationMenu.AppendMenu(490, "End of", endMenu)
		navigationMenu.AppendSeparator()
		navigationMenu.Append(427, "Go to measure/part")

		selectionMenu = wx.Menu()
		selectionMenu.Append(438, "Go to beginning of selection (ctrl+F5)")
		selectionMenu.Append(448, "Go to end of selection (Ctrl+F6)")
		navigationMenu.AppendMenu(428, "Go to selection", selectionMenu)
		
		menuBar.Append(navigationMenu, "&Navigation")

		transcriptionMenu = wx.Menu()
		transcriptionMenu.Append(501, "Transcribe...")
		transcriptionMenu.AppendSeparator()
		transcriptionMenu.AppendRadioItem(601, "Bar-over-bar")
		transcriptionMenu.Check(601, True)
		transcriptionMenu.AppendRadioItem(602, "Line-over-line")
		transcriptionMenu.AppendRadioItem(603, "Section-by-section")
		transcriptionMenu.AppendSeparator()
		transcriptionMenu.Append(604, "Reformat")
		transcriptionMenu.Append(605, "Debugging mode")
		transcriptionMenu.Append(606, "Output interval direction description...")
		transcriptionMenu.Append(607, "Output part list")
		transcriptionMenu.Append(608, "Extract parts...")
		transcriptionMenu.Append(609, "Combine parts to score...")
		menuBar.Append(transcriptionMenu, "&Transcription")

		brailleMusicMenu = wx.Menu()

		inputMenu = wx.Menu()
		brailleMusicMenu.Append(702, "Insert notes (n)")
		brailleMusicMenu.Append(703, "Insert texts (x)")
		brailleMusicMenu.Append(704, "Insert key signature (k)")
		brailleMusicMenu.Append(705, "Insert time signature (t)")
		brailleMusicMenu.Append(706, "Insert chord names and figured bass (c)")
		brailleMusicMenu.Append(707, "Insert title page information (i)")
		brailleMusicMenu.Append(708, "Insert footnotes (o)")
		brailleMusicMenu.Append(709, "Insert division signs (v)")
		brailleMusicMenu.Append(710, "Insert new print page (shift+p)")
		brailleMusicMenu.Append(711, "Insert new braille page (shift+b)")
		brailleMusicMenu.Append(712, "Set current measure (m)")
		brailleMusicMenu.Append(713, "Set current braille page (b)")
		brailleMusicMenu.Append(714, "Set current print page (p)")
		brailleMusicMenu.AppendMenu(701, "Input", inputMenu)
		brailleMusicMenu.Append(715, "Score management...")
		brailleMusicMenu.Append(716, "Part management...")
		brailleMusicMenu.Append(717, "Text management...")
		brailleMusicMenu.Append(718, "Lyrics management...")
		brailleMusicMenu.Append(719, "Chords management...")
		brailleMusicMenu.Append(720, "Metronome management...")
		menuBar.Append(brailleMusicMenu, "&Braille Music")

		playbackMenu = wx.Menu()
		playbackMenu.Append(801, "Play/stop (ctrl+l)")
		playbackMenu.Append(802, "Play current measure (shift+l)")
		playbackMenu.Append(803, "Play current part (ctrl+;)")
		playbackMenu.Append(804, "Play current voice (shift+;)")
		playbackMenu.AppendCheckItem(805, "Play metronome")

		playbackMenu.Append(806, "Choose instruments...")
		playbackMenu.AppendSeparator()
		playbackMenu.AppendCheckItem(807, "Play sounds when navigating")
		playbackMenu.Check(807, True)
		playbackMenu.AppendSeparator()
		playbackMenu.Append(808, "Playback device...")
		menuBar.Append(playbackMenu, "&Playback")

		optionsMenu = wx.Menu()
		optionsMenu.Append(901, "&Options...")

		announceMenu = wx.Menu()
		announceMenu.AppendRadioItem(912, "Silent")
		announceMenu.AppendRadioItem(922, "Braille only")
		announceMenu.AppendRadioItem(932, "Objects only")
		announceMenu.AppendRadioItem(942, "Braille and objects")
		announceMenu.Check(942, True)
		optionsMenu.AppendMenu(902, "Announce modes", announceMenu)
		menuBar.Append(optionsMenu, "&Options")

		windowMenu = wx.Menu()
		windowMenu.Append(1001, "Tile")
		windowMenu.Append(1002, "Cascade")
		windowMenu.AppendSeparator()
		menuBar.Append(windowMenu, "&Window")

		helpMenu = wx.Menu()
		helpMenu.Append(1101, "User manual (F1)")
		helpMenu.Append(1102, "Software website")
		helpMenu.Append(1103, "Check for updates")
		helpMenu.Append(wx.ID_ABOUT, "About...")
		menuBar.Append(helpMenu, "&Help")
		
		self.SetMenuBar(menuBar)
		self.brailleInput = wx.TextCtrl(self, -1, "", size=(200, 100), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_RICH)
		self.CreateStatusBar()
		self.Show(True)
		
		self.brailleInput.SetInsertionPoint(0)
		self.brailleInput.Bind(wx.EVT_KEY_DOWN, self.EvtKeyDown, self.brailleInput)
		self.brailleInput.Bind(wx.EVT_KEY_UP, self.EvtKeyUp, self.brailleInput)

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
			self.brailleInput.WriteText(text)
			self.brailleInput.SetDefaultStyle(wx.TextAttr(wx.RED))
			self.SetStatusText(text)
			self._gesture = None
		return False

app = wx.App(False)
frame = BrailleOrchFrame()
app.MainLoop()