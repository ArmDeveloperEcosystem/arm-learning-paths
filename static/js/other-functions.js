function translateDisplayHoursAndMinutes(totalMinutes) {
    const hours = Math.floor(parseInt(totalMinutes) / 60);
    const minutes = parseInt(totalMinutes) % 60;
    

    let return_str = ''

    // Hours first
    if (hours == 0) {
        return_str = ''
    }
    else if (hours == 1) {
        return_str = hours+' hr'
    }
    else if (hours > 1) {
        return_str = hours+' hrs'
    }

    // Minutes second
    if (minutes == 0) {
        // Add minutes
        return_str = return_str
    }
    else if (( hours != 0) & (minutes != 0) ) {
        // if hours exist, append minuts
        return_str = return_str+' '+minutes+' min'
    }
    else {
        // if minutes exist AND hours are 0, then just display minutes with no space
        return_str = minutes+' min'
    }

    return return_str;
  } // '1 hr 35 min'        '30min'         '1 hr'    '2 hrs 2 min'