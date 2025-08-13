const promptSync = require('prompt-sync')();
const fs = require("fs");
const dotenv = require('dotenv');
dotenv.config();

const OpenAI = require("openai");
const client = new OpenAI();

const SYSTEM_PROMPT = fs.readFileSync("./systemPrompt.txt");;
const PROFILE = fs.readFileSync("./profile.json");
const chatHistory = fs.readFileSync("./_chat.txt");
const currentTime = new Date().toLocaleTimeString();

const prompt = SYSTEM_PROMPT + "\n\n" + PROFILE + "\n\n" + chatHistory + "\n\n" + "Currently Time is: " + currentTime;

let messages = [{ "role": "system", "content": prompt }];

const faizan = async (messages) => {
    const response = await client.chat.completions.create({
        model: "gpt-4.1-mini",
        messages: messages,
    });
    return response.choices[0].message.content;
}



const persona = async () => {
    while (true) {
        let query = await promptSync('> ');
        if(query.toLowerCase() == "stop") {
            break;
        }
        messages.push({ "role": "user", "content": query });
        response = await faizan(messages);
        messages.push({ "role": "assistant", "content": response });
        console.log('> ', response);
    }
}

persona();