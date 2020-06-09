module DataMining
using PlotlyJS
function mine_data()
    # Open data file
    data = undef
    open("data/plgananoparticlestextset.txt") do file
        global data = readlines(file)
    end

    # Figure out where a section starts and ends
    println("Starting")
    sectionIndices = []

    for i = 1:length(data)
        for j = 2:5
            try
                # If the first few characters of the line start with a digit and is followed by a '.' or ':' THEN a ' ', add it.
                isint = false
                try
                    parse(Int, data[i][1:(j-1)])
                    isint = true
                catch err
                    isint = false
                end

                if isint && (data[i][j] == '.' || data[i][j] == ':') && data[i][j+1] == ' '
                    push!(sectionIndices, i)
                    for i = i:length(data)-1
                        secondLine = data[i+1]
                        if secondLine == ""
                            break
                        end # if
                        firstLine = secondLine
                    end # for
                    break
                end # if
            catch
                continue
            end
        end # for
    end # for: O(n) = 4n
    println("Done")
    println(length(sectionIndices))
    scoresarray = []
    # Loop through the sections via sectionIndicices and score it
    for i = 1:4825
        push!(scoresarray, [i, DataMining.score(data[sectionIndices[i]:sectionIndices[i+1]-1])])
    end # for: O(n) =

    # Sort the scoresarray
    sort!(scoresarray, by=a->a[2], rev=true)
    println(scoresarray)

    function get_articletitles(score)
        ids = map(a->a[1], scoresarray[findall(a->a[2]>=score, scoresarray)])

        titles = []
        for id in ids
            push!(titles, data[sectionIndices[id]:sectionIndices[id+1]-1][1])
        end # for
        return titles
    end # function
    
    println(get_articletitles(30))
end # function

function score(article::Array{String})
    # Generate a score based on keywords
    # Keywords Association
    keywords::Dict{String, Int} = Dict(
        "entrapment" => 10,
        "release" => 10,
        "efficiency" => 5,
        "rate" => 5,
        "in vitro" => 2,
        "loaded" => 5,
        "loading" => 2
    )

    # Change the array of sentences to array of unique words
    wordsarray = []

    for group in article
        append!(wordsarray, convert.(String, split(group)))
    end # for
    wordsarray = lowercase.(unique!(wordsarray))

    finalscore = 0
    for word in wordsarray
        for key in keywords
            if key[1] == word
                finalscore += key[2]
            end # if
        end # for
    end # for

    return finalscore

end # function
end # module
