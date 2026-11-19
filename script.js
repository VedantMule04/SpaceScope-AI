
const chatForm = document.getElementById("chatForm");
const questionInput = document.getElementById("questionInput");
const sendButton = document.getElementById("sendButton");

const welcome = document.getElementById("welcome");
const messages = document.getElementById("messages");
const history = document.getElementById("history");

let conversationStarted = false;

// Start a new conversation
function newChat() {
    messages.innerHTML = "";
    messages.style.display = "none";
    welcome.style.display = "block";
    questionInput.value = "";
    conversationStarted = false;
}

// Ask a suggested question
function askSuggestion(question) {
    questionInput.value = question;
    chatForm.requestSubmit();
}

// Create a chat message
function addMessage(sender, text) {
    const message = document.createElement("div");
    message.className = "message";

    const isUser = sender === "You";

    const avatar = document.createElement("div");
    avatar.className = isUser ? "avatar user-avatar" : "avatar";
    avatar.textContent = isUser ? "👤" : "✦";

    const content = document.createElement("div");
    content.className = "message-content";

    const name = document.createElement("div");
    name.className = "message-name";
    name.textContent = isUser ? "You" : "SpaceScope AI";

    const messageText = document.createElement("div");
    messageText.className = "message-text";
    messageText.textContent = text;

    content.appendChild(name);
    content.appendChild(messageText);

    message.appendChild(avatar);
    message.appendChild(content);

    messages.appendChild(message);

    messages.style.display = "flex";

    return messageText;
}

// Update conversation history
function updateHistory(question) {
    if (!conversationStarted) {
        const empty = history.querySelector(".empty-history");
        if (empty) empty.remove();
        conversationStarted = true;
    }

    const item = document.createElement("div");
    item.className = "history-item";
    item.textContent = "✦ " + question;
    history.prepend(item);
}

// Send question to FastAPI
chatForm.addEventListener("submit", async function(event) {
    event.preventDefault();

    const question = questionInput.value.trim();

    if (!question) return;

    welcome.style.display = "none";

    addMessage("You", question);
    updateHistory(question);

    questionInput.value = "";
    questionInput.style.height = "auto";

    sendButton.disabled = true;

    const loadingMessage = addMessage("AI", "Exploring the universe...");

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        if (!response.ok) {
            throw new Error("Server error: " + response.status);
        }

        const data = await response.json();

        loadingMessage.textContent = data.answer;

    } catch (error) {
        loadingMessage.textContent =
            "Sorry! Something went wrong. Please check whether the FastAPI server and Ollama are running.";

        console.error(error);

    } finally {
        sendButton.disabled = false;
        questionInput.focus();
        messages.scrollTop = messages.scrollHeight;
    }
});

// Automatically increase input height
questionInput.addEventListener("input", function() {
    this.style.height = "auto";
    this.style.height = Math.min(this.scrollHeight, 130) + "px";
});

// Send question using Enter
questionInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        chatForm.requestSubmit();
    }
});
