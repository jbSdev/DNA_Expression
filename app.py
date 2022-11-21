from tkinter import *
from tkinter import ttk

def to_uppercase(*args):
	dna.set(dna.get().upper())

def errormsg():
	coding_dna.set('Nieprawidlowy łancuch')
	mRNA.set(' ')
	poli.set(' ')

def checker(input):
	if not input:
		errormsg()
		return False
	
	if any(i not in set('ATCG') for i in input):
		errormsg()
		return False

	return True

	#if input[-3:-1] != ''

def modification():
	input	= str(dna.get())
	
	if checker(input) == False:
		return

	code = ''
	mR = ''
	pl = ''

	for i in input:
		if i == 'A':
			code = code + 'T'
			mR = mR + 'U'
		elif i == 'T':
			code = code + 'A'
			mR = mR + 'A'
		elif i == 'G':
			code = code + 'C'
			mR = mR + 'C'
		elif i == 'C':
			code = code + 'G'
			mR = mR + 'G'

# WHY DO I HAVE TO DO THIS			IT'A F*CKING NIGHTMARE	(and I'm to lazy to change it :D)
	for i in range(0, len(mR), 3):
		if mR[i] == 'U':
			if mR[i + 1] == 'U':
				if mR[i + 2] == 'U' or mR[i + 2] == 'C':
					pl = pl + 'PHE-'
				elif mR[i + 2] == 'A' or mR[i + 2] == 'G':
					pl = pl + 'LEU-'

			elif mR[i + 1] == 'C':
				pl = pl + 'SER-'

			elif mR[i + 1] == 'A':
				if mR[i + 2] == 'U' or mR[i + 2] == 'C':
					pl = pl + 'TYR-'
				elif mR[i + 2] == 'A' or mR[i + 2] == 'G':
					pl = pl + 'STOP'
					break

			elif mR[i + 1] == 'G':
				if mR[i + 2] == 'U' or mR[i + 2] == 'C':
					pl = pl + 'CYS-'
				elif mR[i + 2] == 'A':
					pl = pl + 'STOP'
					break
				elif mR[i + 2] == 'G':
					pl = pl + 'TRP-'
			
		elif mR[i] == 'C':
			if mR[i + 1] == 'U':
				pl = pl + 'LEU-'
			
			elif mR[i + 1] == 'C':
				pl = pl + 'PRO-'
			
			elif mR[i + 1] == 'A':
				if mR[i + 2] == 'U' or mR[i + 2] == 'C':
					pl = pl + 'HIS-'
				elif mR[i + 2] == 'A' or mR[i + 2] == 'G':
					pl = pl + 'GLN-'
				
			elif mR[i + 1] == 'G':
				pl = pl + 'ARG-'

		elif mR[i] == 'A':
			if mR[i + 1] == 'U':
				if mR[i + 2] == 'U' or mR[i + 2] == 'C' or mR[i + 2] == 'A':
					pl = pl + 'ILE-'
				if mR[i + 2] == 'G':
					pl = pl + 'MET-'
			
			elif mR[i + 1] == 'C':
				pl = pl + 'THR-'

			elif mR[i + 1] == 'A':
				if mR[i + 2] == 'U' or mR[i + 2] == 'C':
					pl = pl + 'ASN-'
				elif mR[i + 2] == 'A' or mR[i + 2] == 'G':
					pl = pl + 'LYS-'

			elif mR[i + 1] == 'G':
				if mR[i + 2] == 'U' or mR[i + 2] == 'C':
					pl = pl + 'SER-'
				elif mR[i + 2] == 'A' or mR[i + 2] == 'G':
					pl = pl + 'ARG-'

		elif mR[i] == 'G':
			if mR[i + 1] == 'U':
				pl = pl + 'VAL-'

			elif mR[i + 1] == 'C':
				pl = pl + 'ALA-'

			elif mR[i + 1] == 'A':
				if mR[i + 2] == 'U' or mR[i + 2] == 'C':
					pl = pl + 'ASP-'
				elif mR[i + 2] == 'A' or mR[i + 2] == 'G':
					pl = pl + 'GLU-'

			elif mR[i + 1] == 'G':
				pl = pl + 'GLY-'
		
	if pl[-4:] != 'STOP':
		print("No STOP callsign\n")
		errormsg()
		mRNA.set('Brak grupy \'STOP\'')
		return
	
	coding_dna	.set('5\'' + code + '3\'')
	mRNA		.set('5\'' + mR + '3\'')
	poli		.set(pl)


root = Tk()
root.title('Ekspresja DNA - Antoni Jesień 3C')
root.geometry("500x200")
root.configure(bg = '#f0f0f0')

mainframe = ttk.Frame(root, padding = '12 12 3 3')
mainframe.grid(column = 0, row = 0, sticky = (N, W, S, E))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 2)

#region ENTRY STRING

dna_label = ttk.Label(mainframe, text = 'Wpisz łancuch DNA: ')
dna_label.grid(column = 0, row = 0)

dna = StringVar()
dna_entry = ttk.Entry(mainframe, width = 30, textvariable = dna)
dna_entry.grid(column = 1, row = 0, sticky = (W, E))

# all uppercase
try:
	# python 3.6
	dna.trace_add('write', to_uppercase)
except AttributeError:
	# python < 3.6
	dna.trace('w', to_uppercase)
#endregion

#region CODING STRING

coding_intro = ttk.Label(mainframe, text = 'Nić kodujaca: ')
coding_intro.grid(column = 0, row = 2)

coding_dna = StringVar()

coding_out = ttk.Label(mainframe, textvariable = coding_dna)
coding_out.grid(column = 1, row = 2)
#endregion

#region mRNA STRING

mRNA_intro = ttk.Label(mainframe, text = 'mRNA: ')
mRNA_intro.grid(column = 0, row = 3)

mRNA = StringVar()

mRNA_out = ttk.Label(mainframe, textvariable = mRNA)
mRNA_out.grid(column = 1, row = 3)
#endregion

#region POLIPEPTIDE

poli_intro = ttk.Label(mainframe, text = 'Łancuch polipeptydowy: ')
poli_intro.grid(column = 0, row = 4)

poli = StringVar()

poli_out = ttk.Label(mainframe, textvariable = poli)
poli_out.grid(column = 1, row = 4)
#endregion

#region CALCULATE

button_text = StringVar()
button_text.set('Oblicz:')

calculate = ttk.Button(mainframe, textvariable = button_text, command = modification)
calculate.grid(column = 1, row = 1)
#endregion

# ADDITIONS

for child in mainframe.winfo_children(): 
	child.grid_configure(padx = 5, pady = 5)

dna_entry.focus()

root.mainloop()