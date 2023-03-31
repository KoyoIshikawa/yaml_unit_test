// Notion Add Page to Databse + MD 

// adds page to notion db with MD converted to Notion block types

// Updated 22/3/22 - change to block properties

// Assumes that the title property of your db pages default is "Name", if not, change below

// Enter your database ID below

  

/* ----- database id: paste ID between "quotes" -----*/

const dbid = "94bf99ed50164e61bf291907936b867d"; // from db page link, between last "/" and "?"

  

// endpoint url

const endpoint = "https://api.notion.com/v1/pages";

  

//get draft title + content, remove blank lines

const lines = draft.content.replace(/$\s*\n+/gm, "\n").trim().split('\n'); 

  

const title = lines.shift().replace(/^# /, "");

  

// create page

const parent = { "database_id": dbid };

  

//"Name" refers to the title property of your db pages, default is "Name", if you have changed this, replace "Name" below

const properties = { 

"Name": { "title": [ {"text": { "content": title}}]} ,

"Google連携": {"multi_select": [ {"name": "🗓カレンダー"}]},

};

  

const children = [];

  

const page = { parent, properties, children }; 

  

//-----------------

  

function addBlock(line){

  

const block = {"object": "block", "type" : "paragraph"};

const anyPref = /^(\s*([-*+]|#+)\s+)/;

  

// map prefix to block type

const types = new Map ([ 

["to_do", /^(\s[*-*+]\s\[\s]\s+)/],

["bulleted_list_item", /^(\s[*-*+]\s+)/],

["heading_3", /^(\s*###\s+)/], 

["heading_2", /^(\s*##\s+)/],

["heading_1", /^(\s*#\s+)/], 

]);

  

// if any prefix

if (anyPref.test(line)) {

  

// get type

types.forEach( ( reg, name ) => {

if (reg.test(line)) {

block.type = name;

line = line.replace(reg, ""); 

}})

}

// complete block

block[block.type] = {"rich_text": [{ "type": "text", 

"text": { "content" : line }}]};

  

children.push(block);

}

  

// ---------------------

  

//if lines, add child blocks

if (lines) {

lines.forEach(addBlock);

  

} 

  

// create Notion instance to make request

let notion = Notion.create();

let response = notion.request({

"url": endpoint,

"method": "POST",

"data": page

});

  

// result 

if (!response.statusCode == 200) {

  

alert(`Notion Error: ${response.statusCode}

${notion.lastError}`);

context.fail();

}

  

