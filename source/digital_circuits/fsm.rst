=====================
Finite State Machines
=====================

Verilog Template
----------------

.. code::

    module fsm_template (
        input wire clk_slow, reset_n,

        // inputs 
        input wire i_input_signal, 

        // outputs
        output reg o_output_signal,   

    ); 

    // State name definitions
    typedef enum logic[1:0] {STATE_1,
                             STATE_2,
                             STATE_3,
                             STATE_4,
                             } em_state;
    em_state state, state_next;

    // Timer
    reg [7:0] timer;  // Resize to store the max value of the timers below
    localparam T_WAIT = 128;

    // Sequential logic to update state
    always @(posedge clk or negedge reset_n) begin : proc_state_change
        if(!reset_n) begin
            state <= STATE_1;
        end else begin
            state <= state_next;
        end
    end

    // Combinational logic to update next state, and the outputs in each state
    always_comb begin : proc_next_state_and_output

        // Default next state is current state
        state_next = state;

        // Default outputs
        o_output_signal = 0

        case (state)
            STATE_1    : begin 
                            o_output_signal = 1;

                            state_next = STATE_2;
                         end
            STATE_2    : begin 
                            if (i_input_signal) begin
                                o_output_signal = 1;
                            end

                            state_next = STATE_3;
                         end
            STATE_3    : begin 
                            if (timer > T_WAIT) begin
                                state_next = STATE_4;
                            end
                         end
            STATE_4    : begin 
                            state_next = STATE_1;
                         end

            default    : begin 
                            state_next = STATE_1;
                         end
        endcase
    end


    // Timer 
    always @(posedge clk or negedge reset_n) begin 
        if (!reset_n) begin
            timer <= 0;
        end
        else begin
            if (state != state_next) begin  // state is changing
                timer <= 0;
            end
            else begin
                timer <= timer + 1;  
            end
        end
    end

    endmodule // fsm_template
