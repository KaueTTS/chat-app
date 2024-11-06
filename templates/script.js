const socket = io()
const chatMessages = document.getElementById("chat-messages")
const messageInput = document.getElementById("message-input")
const sendButton = document.getElementById("send-button")
const currentUsernameSpan = document.getElementById("current-username")
const usernameInput = document.getElementById("username-input")
const updateUsernameButton = document.getElementById("update-username-button")

let currentUsername = ""

socket.on("set_username", (data) => {
    currentUsername = data.username
    currentUsernameSpan.textContent = `Your username: ${currentUsername}`
})

socket.on("user_joined", data => {
    addMessage(`${data.username} joined the chat`, "system")
})