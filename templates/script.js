const socket = io()
const chatMessages = document.getElementById("chat-messages")
const messageInput = document.getElementById("message-input")
const sendButton = document.getElementById("send-button")
const currentUsernameSpan = document.getElementById("current-username")
const usernameInput = document.getElementById("username-input")
const updateUsernameButton = document.getElementById("update-username-button")

let currentUsername = ""