// Subscribe once swampdragon is connected
swampdragon.open(function () {
    swampdragon.subscribe('calculations', 'calculations');
});

// This is the list of notifications
// var notificationsList = $("#notifications");
var notificationsList = document.getElementById('notifications')


// New channel message received
swampdragon.onChannelMessage(function (channels, message) {
    // Add the notification
    if (message.action === "created") {
        addNotification((message.data));
    }
});



// Add new notifications
function addNotification(notification) {
    // Add the new notification
    var li = document.createElement("li");
    li.innerHTML = notification.expression + ' = ' + notification.result;
    // notificationsList.insertBefore(li, notificationsList.firstChild).hide().show('slow');
    notificationsList.insertBefore(li, notificationsList.firstChild);

    // Remove excess notifications
    while (notificationsList.getElementsByTagName("li").length > 10) {
        notificationsList.getElementsByTagName("li")[10].remove();
    }
}
