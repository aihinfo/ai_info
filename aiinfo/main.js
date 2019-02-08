const electron = require('electron');
const url = require('url');
const path = require('path');
const {app, BrowserWindow, Menu}= electron;

let mainWindow;

function createAddwindow(){
	mainWindow = new BrowserWindow({title:'add new sho'});
	//mainWindow = new BrowserWindow({width:800, height:600})
	//mainWindow.loadFile('index.html')

	// Load html into window
	mainWindow.loadURL(url.format({
		pathname: path.join(__dirname, 'index.html'),
		protocol: 'file:', //file//dirname/index.html
		slashes: true
	}));
}
// listen for app to be ready
app.on('ready', function(){
	// create new window
	mainWindow = new BrowserWindow({});
	//mainWindow = new BrowserWindow({width:800, height:600})
	//mainWindow.loadFile('index.html')

	// Load html into window
	mainWindow.loadURL(url.format({
		pathname: path.join(__dirname, 'index.html'),
		protocol: 'file:', //file//dirname/index.html
		slashes: true
	}));
	//create menu template
	const mainMenuTemplate =[
		{
			label:'File',
			submenu:[
			{
				label: 'Add Item'
			},
			{
				label: 'Add Item2'
			}
			]
		}
	];
const template = [
    {
  	label: 'file',
    click(){createAddwindow();}
 	},
  {
    label: 'View',
    submenu: [
      { role: 'reload' },
      { type: 'separator' }
    ]
  },
  {
    role: 'help',
    submenu: [
      {
        label: 'Learn More',
        //click () { require('electron').shell.openExternal('https://electronjs.org') }
      	click(){createAddwindow();}
      }
    ]
  },
]

	//build menu from template
	//insert menu
	const menu = Menu.buildFromTemplate(template)
	Menu.setApplicationMenu(menu)

});

