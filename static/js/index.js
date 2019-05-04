// intitialise global variables

const recipe_likes = [1,1111,999]
localStorage.setItem('user_likes', ['likes'])

const add_like = (title, author, id) =>{
    const like = {title, author, id};
    recipe_likes.push(like);
    
}

const remove_like = id =>{
    const like = id;
    recipe_likes.splice(id);
}