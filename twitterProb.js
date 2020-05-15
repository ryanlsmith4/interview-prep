// Twitter problem done in javascript!

const getCount = (handle, handles, k = 1) => {
   let handleChars = new Object();
   let scoreDict = new Object(); 
    for (let i = 0; i < handle.length; i++){
        handleChars[handle[i].toLowerCase()] = 0
    };
    for (let i = 0; i < handles.length; i++){
        let currHandle = handles[i].toLowerCase()
        let key;
        for (let j = 0; j < currHandle.length; j++){
            if (currHandle[j] in handleChars){
                key = currHandle[j]
                handleChars[key] += 1
            } else {
                handleChars[key] -= 1
            }
        } scoreDict[currHandle] = handleChars[key]
    }
    let values = Object.values(scoreDict);
    let max;
    let index;
    let kValues = new Array()
    for(let i = 0; i < k; i++){
         max = Math.max(...values)
         index = values.indexOf(max)
         values.splice(index)
         kValues.push(index)
    }
    let keys = Object.keys(scoreDict)
    let solution = new Array()
    for(let i = 0; i < kValues.length; i++) {
        solution.push(keys[kValues[i]])
    }
    return solution;
}

const handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
console.log(getCount('iLoveDogs', handles, 2))