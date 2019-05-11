// intitialise global variables


let userData = {};
let userLikes;
let isLiked = false;
let handleLikeState = (id, currentLikes, title, likeState) => {
    const oldLikes = JSON.parse(localStorage.getItem('activeUser'));
    const liked = { id, title };

    if (oldLikes.userLikes.length === 0) {
        currentLikes.userLikes.push(id);
        console.log('Will update likes because i have a new id: ', oldLikes);
        localStorage.setItem('activeUser', JSON.stringify(currentLikes))

    }
    else {

        for (let i = 0; i < oldLikes.userLikes.length; i++) {
            if (oldLikes.userLikes[i].id == id) {
                console.log('Recipe has been liked already so wont update like: ', currentLikes);
            }
            else {
                currentLikes.userLikes.push(id);
                console.log('Will update likes because i have a new id: ', currentLikes);
                localStorage.setItem('activeUser', JSON.stringify(currentLikes))
                for (let i = 0; i < currentLikes.userLikes.length; i++) {
                    if (currentLikes.userLikes[i].id == id) {
                        console.log('Updating: ', currentLikes);
                    }
                }
            }
        }
    }




};

const remove_like = id => {
    userLikes.splice(id);
};

const login = () => {
    let activeUser = document.getElementById("username").value;
    Object.assign(userData, { username: activeUser }, { userLikes: [], status: isLiked }),
        localStorage.setItem('activeUser', JSON.stringify(userData));
    console.log(userData);
};

const logout = () => {
    // localStorage.removeItem("userData");
};

const add_like = () => {
    const signedIn = JSON.parse(localStorage.getItem('activeUser'));
    const id = window.location.href;
    const title = document.getElementById("title").innerHTML;

    if (signedIn) {
        handleLikeState(id, signedIn, title, isLiked)
    };
};


