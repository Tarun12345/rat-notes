// Gulpfile.js
// Require the needed packages
var gulp = require('gulp');
var gutil = require('gulp-util');
var stylus = require('gulp-stylus');
var concat = require('gulp-concat');


// Get one .styl file and render
gulp.task('css', function () {
    gulp.src('./note/static/styl/style.styl')
        .pipe(stylus())
    	.pipe(concat("style.css"))
        .pipe(gulp.dest('./note/static/css'));
});


// Default gulp task to run
gulp.task('default', function(){
    gulp.run('css');
});