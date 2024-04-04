const addExercise = document.getElementById('addExercise');
addExercise.addEventListener('click', function() {
    // pop up a form with exercise name, sets, reps, weight
    document.getElementById('exerciseForm').style.display = 'block';

    // add the exercise to the list of exercises
    const exerciseList = document.getElementById('exerciseList');
    const exercise = document.createElement('li');
    exercise.textContent = 'Exercise Name';
    exerciseList.appendChild(exercise);

    // add the exercise to the database
    const exerciseName = document.getElementById('exerciseName').value;
    const sets = document.getElementById('sets').value;
    const reps = document.getElementById('reps').value;
    const weight = document.getElementById('weight').value;
    
    const data = {
        exerciseName: exerciseName,
        sets: sets,
        reps: reps,
        weight: weight
    };
    
    doc_ref = db.collection('user_exercises').document();
    doc_ref.set({ 
        'email': formName['data in form'], 
        'first_name': user_profile_data['first_name'], 
        'last_name': user_profile_data['last_name'] 
    });
    // update the workout display
});